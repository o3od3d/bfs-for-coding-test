"""
1. 아이디어
 - 2 중 for문 = > 방문x & 값 2x
 - 1,2,3...순서로 진행
 - 베이스캠프 - 거리짧고 행 열 작은 순ㄴ
 - 편의점 - 거리짧고 상,좌,우,하 순

2. 시간복잡도
 - O(M*(V+E)) = 30 * 5V = 33750 < 2억
 - V : 15 * 15
 - E : 4V

3. 자료구조
 - 그래프 : INT[][]
 - 방문 : INT[][]
 - BFS : QUEUE
"""
from collections import deque
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
end = []
for i in range(m):
    x,y = map(int,input().split())
    end.append([x-1,y-1])
direction = [[-1,0],[0,-1],[0,1],[1,0]]

# 베이스 캠프 위치 담기
base = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            base.append([i,j])

# 베이스 캠프 찾기
def basecamp(x,y):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    res = []
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        if [x,y] in base:
            res.append([visited[x][y],x,y])
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and board[nx][ny] != 2:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
    return sorted(res,key=lambda x:(-x[0],-x[1],-x[2]))

# 편의점 위치 찾기
def store(x,y,ex,ey):
    q = deque()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q.append([x,y])
    visited[x][y] = 1
    res = []

    while q:
        x,y = q.popleft()
        if [x,y] == [ex,ey]:
            return visited[x][y]
        for dir in range(len(direction)):
            nx = x + direction[dir][0]
            ny = y + direction[dir][1]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 2 and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1

    return 1e9
t = 0
# 현위치
cur = []
cnt2 = 0
cnt = 0
while True:
    if t > 0:
        for i in range(cnt,cnt2):

            minNum = 1e9
            x,y = cur[i][0],cur[i][1]
            ex,ey = end[i][0],end[i][1]
            for k in range(4):
                nnx = x + direction[k][0]
                nny = y + direction[k][1]
                if 0 <= nnx < n and 0 <= nny < n and board[nnx][nny] != 2:
                    res = store(nnx,nny,ex,ey)
                    if minNum > res:
                        minNum = res
                        nextdire = k

            cur[i] = [x + direction[nextdire][0],y+direction[nextdire][1]]
            if cur[i] == end[i]:
                board[cur[i][0]][cur[i][1]] = 2
                cnt += 1


    # 베이스 캠프
    if t < m:
        cnt2 += 1
        x,y = end[t][0], end[t][1]
        res = basecamp(x,y)
        _,x,y = res.pop()
        cur.append([x,y])
        base.remove([x,y])
        board[x][y] = 2

    t += 1
    # 종료조건
    if cnt == m:
        print(t)
        break