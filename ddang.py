N,M,K = map(int,input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        board[i][j].append(tmp[j])
pos = []
dire = []
skill = []
for _ in range(M):
    x,y,d,s = map(int,input().split())
    pos.append([x-1,y-1])
    dire.append(d)
    skill.append(s)
direction = [[-1,0],[0,1],[1,0],[0,-1]]
points = [0] * M
guns = [0] * M

def chkGun(i,j,m):

    for b in range(len(board[i][j])):
        if guns[m] < board[i][j][b]:
            tmp = guns[m]
            guns[m] = board[i][j][b]
            board[i][j][b] = tmp

def winPlayer(pow1,pow2,idx1,idx2):
    points[idx1] += abs(pow1 - pow2)
    if guns[idx2] != 0:
        board[x][y].append(guns[idx2])
        guns[idx2] = 0
    d_tmp = dire[idx2]
    while True:
        nx, ny = x + direction[d_tmp][0], y + direction[d_tmp][1]
        if 0 <= nx < N and 0 <= ny < N and [nx, ny] not in pos:
            pos[idx2] = [nx, ny]
            break
        else:
            d_tmp = (d_tmp + 1) % 4
            dire[idx2] = d_tmp

    lx, ly = pos[idx2]
    chkGun(lx, ly, idx2)
    chkGun(x, y, idx1)
for _ in range(K):
    for m in range(M):
        # 1-1 이동
        x,y = pos[m]
        nx = x + direction[dire[m]][0]
        ny = y + direction[dire[m]][1]
        if 0 <= nx < N and 0 <= ny < N:
            x,y = nx,ny
        else:
            d_tmp = (dire[m] + 2) % 4
            x = x + direction[d_tmp][0]
            y = y + direction[d_tmp][1]
            dire[m] = d_tmp
        # 2-1. 이동한 곳에 플레이어 없는 경우
        if [x,y] not in pos:
            chkGun(x,y,m)
            pos[m] = [x, y]
        # 2-2. 플레이어 있는 경우
        else:

            p1 = guns[m] + skill[m]
            idx = pos.index([x,y])
            p2 = guns[idx] + skill[idx]
            pos[m] = [x, y]
            if p1 > p2:
                winPlayer(p1,p2,m,idx)
            elif p1 < p2:
                winPlayer(p2,p1,idx,m)
            else:
                if skill[m] > skill[idx]:
                    winPlayer(p1,p2,m,idx)
                else:
                    winPlayer(p2,p1,idx,m)

print(' '.join(map(str,points)))
