"""
nxn크기 m마리물고기 1마리 아기상어
아기상어크기2
1초 상하좌우 인접 1칸 이동
자신보다 크기 큰 물고기 지나갈 수 없다.
자신보다 크기 작은 물고기만 먹는다.
- 더이상 먹을 수 있는 물고기 없으면 엄마에게 도움요청
- 먹을 수 있는 고기 1마리 먹는다.
- 1마리 이상이면, 가장 가깝고, 행 작고, 열작은 물고기 먹는다.
크기와 같은 수 물고기 먹을 때마다 크기 1 증가

1. 아이디어
 - 2 중 for문 -> 크기가 같거나 작은칸 & 방문x
 - 크기 작으면 배열에 담고 그중 가깝고 행작고 열작은 물고기 선택하고 위치 이동
 - 크기 증가 시킴

2. 시간복잡도
 - O(V+E)
 - V : 20 * 20
 - E : 4V

3. 자료구조
 - 그래프 : INT[][]
 - BFS : QUEUE
 - 방문 : INT[][]
"""
from collections import deque
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
size = 2
direction = [[0,1],[0,-1],[1,0],[-1,0]]
ans = 0
eat = 0
# 상어 위치 찾고 9를 0으로 변경
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            sx,sy = i,j
            board[i][j] = 0
            break

#1초 상하좌우 인접 1칸 이동
def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0
    res = []
    while q:
        x,y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] <= size and visited[nx][ny] == -1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
                    if 0 < board[nx][ny] < size:
                        res.append([visited[nx][ny],nx,ny])

    return sorted(res,key=lambda x:(-x[0],-x[1],-x[2]))

while True:
    res = bfs(sx,sy)

    # - 더이상 먹을 수 있는 물고기 없으면 엄마에게 도움요청
    if len(res) == 0:
        print(ans)
        break
    # - 먹을 수 있는 고기 1마리 먹는다.
    # - 1마리 이상이면, 가장 가깝고, 행 작고, 열작은 물고기 먹는다.

    dis,sx,sy = res.pop()
    eat += 1
    ans += dis
    board[sx][sy] = 0
    #크기와 같은 수 물고기 먹을 때마다 크기 1 증가
    if eat == size:
        eat = 0
        size += 1