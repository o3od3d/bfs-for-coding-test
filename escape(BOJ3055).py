"""
고슴도치 S 비버굴 D 돌 X 물 * 빈.
매분 고슴도치 상하좌우 한칸 비버굴향해
물 - 돌,비버 X
고슴도치 - 물,돌 X

최소시간? 안되면 "KAKTUS"

1. 아이디어
 - 2 중 FOR문 = > 고슴도치 - 물X&돌X &방문 X
 - 2 중 FOR문 => 물 - 돌X

2. 시간복잡도
 - O (V+E)
 - V : 50 * 50
 -E : 4V

3. 자료구조
 - 그래프 : INT[][]
 - QUEUE
"""
from collections import deque
R,C = map(int,input().split())
board = [list(map(str,input().strip())) for _ in range(R)]
q = deque()
dx,dy = (1,-1,0,0),(0,0,1,-1)
visited = [[-1] * C for _ in range(R)]
# 고슴도치 & 물의 위치
for i in range(R):
    for j in range(C):
        if board[i][j] == 'D':
            ex,ey = i,j
        elif board[i][j] == 'S':
            q.append([i,j])
            visited[i][j] = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        if board[ex][ey] == 'S':
            return visited[ex][ey]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C:
                # 고슴도치
                if board[x][y] == 'S' and visited[nx][ny] == -1 and (board[nx][ny] == 'D' or board[nx][ny] == '.'):
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
                    board[nx][ny] = 'S'
                elif board[x][y] == '*' and (board[nx][ny] == '.' or board[nx][ny] == 'S'):
                    q.append([nx,ny])
                    board[nx][ny] = '*'
    return -1
ans = bfs()
if ans == -1:
    print('KAKTUS')
else:
    print(ans)