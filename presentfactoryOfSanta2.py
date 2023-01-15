"""
리스트를 이용해서 해당의 지문앞 = 뒤를 이용하여 푼다.

1. 공장 설립
 -

"""
import math

q = int(input())
tmp = list(map(int,input().split()))
n,m = tmp[1],tmp[2]
belts = tmp[3:]
com = [list(map(int,input().split())) for _ in range(q-1)]

# 1. 공장 설립
def establish():
    belt = [[] for _ in range(n+1)]
    for i in range(m,0,-1):
        belt[belts[i-1]].append(i)
    return belt

# 2. 물건 모두 옮기기
def moveStaff(m_src,m_dst):
    if len(belt[m_src]) != 0:
        for i in belt[m_src]:
            belt[m_dst].append(i)
        belt[m_src] = []
    print(len(belt[m_dst]))

# 3. 앞 물건만 교체
def front(m_src,m_dst):
    tmp,tmp2 = 0,0
    if len(belt[m_src]) != 0:
        tmp = belt[m_src].pop()
    if len(belt[m_dst]) != 0:
        tmp2 = belt[m_dst].pop()
    if tmp != 0:
        belt[m_dst].append(tmp)
    if tmp2 != 0:
        belt[m_src].append(tmp2)
    print(len(belt[m_dst]))

# 4. 물건 나누기
def divideStaff(m_src,m_dst):
    if len(belt[m_src]) > 1:
        tmp = math.floor(len(belt[m_src])/2)
        res = []
        for _ in range(tmp):
            res.append(belt[m_src].pop())
        for i in range(tmp-1,-1,-1):
            belt[m_dst].append(res[i])
    print(len(belt[m_dst]))

# 선물 정보 얻기
def presentInfo(p_num):
    for i in range(1,n+1):
        for j in range(len(belt[i])):
            if belt[i][j] == p_num:
                x,y = i,j
    # 앞 번호
    if y != len(belt[x])-1:
        a = belt[x][y+1]
    else:
        a = -1
    # 뒤 번호
    if y != 0:
        b = belt[x][y-1]
    else:
        b = -1
    print(a+2*b)

# 벨트 정보 얻기
def beltInfo(b_num):
    if len(belt[b_num]) != 0:
        a = belt[b_num][-1]
        b = belt[b_num][0]
    else:
        a,b = -1,-1
    print(a+2*b+3*len(belt[b_num]))

belt = establish()

for c in range(q-1):
    if com[c][0] == 200:
        moveStaff(com[c][1],com[c][2])
    elif com[c][0] == 300:
        front(com[c][1],com[c][2])
    elif com[c][0] == 400:
        divideStaff(com[c][1],com[c][2])
    elif com[c][0] == 500:
        presentInfo(com[c][1])
    elif com[c][0] == 600:
        beltInfo(com[c][1])


