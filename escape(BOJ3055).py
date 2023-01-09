"""
고슴도치 1마리
비버 굴 1개
고슴도치 홍수 피하기
. 빈칸 * 물 X 돌 D 비버 굴 S 고슴도치 위치
매 분마다 고슴도치는 인접 1칸 이동 물도 인접 빈칸으로 확장
물은 돌과 굴 이동 불가
고슴도치는 물과 돌, 다음에 물이 찰칸 이동불가
고슴도치가 피하기 위한 최소 시간

1. 아이디어
  - 2 중 FOR 문 => 물은 돌,굴 피해 인접칸 확장
  고슴도치는 물,돌 다음 물칸 이동 불가
  - D에 고슴도치 도착 시간 출력 OR 이동 불가면 KAKTUS 출력

2. 시간복잡도
 - O(V+E)
 - V : 50 * 50
 - E : 4V

3. 자료구조
 - GRAPH : STR[][]
 - 방문 : INT[][]
 - QUEUE :

"""
from collections import deque
R,C = map(int,input().split())
board = [list(map(str,input().strip())) for _ in range(R)]
q = deque()
direction = [[0,1],[0,-1],[1,0],[-1,0]]
visited = [[0] * C for _ in range(R)]

# 고슴도치 위치, 비버 굴 위치
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            q.append([i,j])
        elif board[i][j] == 'D':
            ex,ey = i,j

# 물 위치 큐에 담기
for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        if board[ex][ey] == 'S':
            return visited[ex][ey]
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < R and 0 <= ny < C:
                # 고슴도치
                if board[x][y] == 'S' and (board[nx][ny] == '.' or board[nx][ny] == 'D'):
                    q.append([nx,ny])
                    board[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                # 물
                elif board[x][y] == '*' and (board[nx][ny] == '.' or board[nx][ny] == 'S'):
                    board[nx][ny] = '*'
                    q.append([nx,ny])
    return 'KAKTUS'
print(bfs())