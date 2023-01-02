"""
1. 아이디어
 -

2. 시간복잡도
 - O(V+E) 500 +

3. 자료구조
 - graph[][]
 - Queue
 - visited[][]

"""
from collections import deque

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
q = deque()
direction = [[0,1],[0,-1],[1,0],[-1,0]]
visited = [[False] * m for _ in range(n)]
def bfs(x,y):
    global visited
    visited[x][y] = True
    q.append([x,y])
    cnt = 1
    while q:
        x,y = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

res = 0
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            ans = max(ans,bfs(i,j))
            res += 1
print(res)
print(ans)