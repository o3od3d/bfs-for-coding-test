"""
불 - 매초 동서남북
상근 - 벽x 불x, 불 붙으려는 칸 x

"""
from collections import deque
T = int(input())
dx,dy = (1,-1,0,0),(0,0,1,-1)
def bfs():
    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                # 상근이
                if board[x][y] == '@' and visited[nx][ny] == -1 and board[nx][ny] == '.':
                    q.append([nx,ny])
                    board[nx][ny] = '@'
                    visited[nx][ny] = visited[x][y] + 1
                elif board[x][y] == '*' and (board[nx][ny] == '.' or board[nx][ny] == '@'):
                    q.append([nx,ny])
                    board[nx][ny] = '*'
            else:
                if board[x][y] == '@':
                    return visited[x][y]
    return -1

for t in range(T):
    w,h = map(int,input().split())
    board = [list(map(str,input().strip())) for _ in range(h)]
    q = deque()
    visited = [[-1] * w for _ in range(h)]

    # 상근이 위치
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                q.append([i,j])
                visited[i][j] = 1
                break

    # 불 위치
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                q.append([i,j])


    ans = bfs()
    if ans == -1:
        print('IMPOSSIBLE')
    else:
        print(ans)