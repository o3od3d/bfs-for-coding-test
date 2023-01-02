"""
1. 아이디어
 - 3 중 FOR 문 :
 - 토마토 최소 걸리는 일 수? 모두 익어있으면 0, 모두 익지 못하면 -1

2. 시간복잡도 :
 - O(V+E) = 7V = 1000000 < 2억 가능
 - V : 100 * 100 * 100
 - E : 6V

3. 자료구조
 - GRAPH : int[][][]
 - visited : bool[][][]
 - queue
"""
from collections import deque
M,N,H = map(int,input().split())
graph = [[] * N for _ in range(H)]
for h in range(H):
    for n in range(N):
        graph[h].append(list(map(int,input().split())))
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
direction = [[0,1,0],[0,-1,0],[1,0,0],[-1,0,0],[0,0,1],[0,0,-1]]
q = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                q.append([h,n,m])

def bfs():
    while q:
        h,n,m = q.popleft()
        for dir in direction:
            nn = n + dir[0]
            nm = m + dir[1]
            nh = h + dir[2]
            if 0 <= nn < N and 0 <= nm < M and 0 <= nh < H:
                if graph[nh][nn][nm] == 0:
                    q.append([nh,nn,nm])
                    visited[nh][nn][nm] = visited[h][n][m] + 1
                    graph[nh][nn][nm] = 1

bfs()
tomato = 0
cnt = 0
for h in range(H):
    for n in range(N):
        tmp = max(visited[h][n])
        cnt = max(cnt,tmp)

for h in range(H):
    for n in range(N):
        tomato += graph[h][n].count(0)
if tomato == 0:
    print(cnt)
else:
    print(-1)

