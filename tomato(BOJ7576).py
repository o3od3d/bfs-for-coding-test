"""
1. 아이디어
 - 2 중 FOR 문 :
 - 토마토 최소 걸리는 일 수? 모두 익어있으면 0, 모두 익지 못하면 -1

2. 시간복잡도 :
 - O(V+E) = 5V = 1000000 < 2억 가능
 - V : 1000 * 1000
 - E : 4V

3. 자료구조
 - GRAPH : int[][]
 - visited : int[][]
 - queue
"""
from collections import deque

M,N = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
visited = [[0] * M for _ in range(N)]
direction = [[0,1],[0,-1],[1,0],[-1,0]]
q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                    graph[nx][ny] = 1

bfs()
cnt = 0
tomato = 0
# 최소 일수
for v in visited:
    tmp = max(v)
    cnt = max(cnt,tmp)
for g in graph:
    tomato += g.count(0)
if tomato == 0:
    print(cnt)
else:
    print(-1)
#