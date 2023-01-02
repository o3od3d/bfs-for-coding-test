"""
- 아기상어 초기 크기 2 , 1초에 상하좌우 1칸 이동
- 아기 상어는 크기 큰 물고기 칸 지나갈 수 x, 크기 작은 물고기 먹음
- 같은 크기 물고기는 지나가기만 가능
- 아기 상어 이동 규칙
    먹을 수 있는 물고기 x 종료
    1마리면 먹는다.
    1마리 이상이면, 가장 가깝고 <- 가장 위 <- 가장 왼쪽
- 아기 상어 자신의 크기가 같은 물고기 수 먹으면 크기 1 증가

1. 아이디어
 - 2 중 for 문 크기 작은 물고기 중 가장 가깝고 가장 위 가장 왼쪽 물고기 선택한다.


2. 시간복잡도
 -
3. 자료구조
 -
"""
from collections import deque
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
size = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            x,y = i,j
            break
q = deque()
direction = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(sx,sy):
    q.append([sx,sy])
    res = []
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1
    while q:
        x,y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < N:
                if 0 <= board[nx][ny] <= size and visited[nx][ny] == 0:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
                    if 0 < board[nx][ny] < size:
                        res.append([nx,ny,visited[nx][ny]])
    return sorted(res,key=lambda x:(-x[2],-x[0],-x[1]))
ans = 0
cnt = 0
while True:

    # 물고기 먹기
    result = bfs(x,y)
    # 종료 조건
    if len(result) == 0:
        break
    nx,ny,tmp = result.pop()
    ans += (tmp-1)

    board[nx][ny] = 0
    cnt += 1
    x,y = nx,ny
    # 크기 키우기
    if size == cnt:
        size += 1
        cnt = 0
print(ans)