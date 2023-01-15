"""
지훈이 미로에서 탈출
지훈이가 불이 타기전에 탈출할 수 있는지, 얼마나 빨리 탈출할 수 있는지 구하기
불은 매 분마다 한칸씩 수직, 수평이동 즉, 상하좌우 네 방향 이동
지훈이는 미로의 가장자리에 접한 공간에서 탈출 가능하며, 불과 벽으로 이동 불가

1. 아이디어
 - 2 중 FOR문 => 지훈 - 빈칸  & 방문 X
 - 2 중 FOR문 => 불 - 빈칸 OR 지훈

2. 시간복잡도
 - O(V+E) = 5V = 5 * 1000000  < 2억 가능
 - V : 1000 * 1000
 - E : 4V

3. 자료구조
 - 그래프 : str[][]
 - 방문 : int[][]
 - bfs : queue
"""
from collections import deque
R,C = map(int,input().split())
board = [list(map(str,input().strip())) for _ in range(R)]
q = deque()
visited = [[-1] * C for _ in range(R)]
direction = [[0,1],[0,-1],[1,0],[-1,0]]
# 지훈이 위치
for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            q.append([i,j])
            visited[i][j] = 1
            break
# 불 위치
for i in range(R):
    for j in range(C):
        if board[i][j] == 'F':
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < R and 0 <= ny < C:
                # 지훈이
                if board[x][y] == 'J' and visited[nx][ny] == -1 and board[nx][ny] == '.':
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
                    board[nx][ny] = 'J'
                # 불
                elif board[x][y] == 'F' and (board[nx][ny] == '.' or board[nx][ny] == 'J'):
                    q.append([nx,ny])
                    board[nx][ny] = 'F'
            else:
                if board[x][y] == 'J':
                    return visited[x][y]
    return 'IMPOSSIBLE'
print(bfs())