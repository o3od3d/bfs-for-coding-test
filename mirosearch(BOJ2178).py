"""
1. 아이디어
 - 이중 for 문 => 값 1 && 방문 x
 - 도착 최소 칸 수

2. 시간복잡도
 - O(V+E) = 50000 < 2억 가능
 - V : 100 * 100
 - E : 4V

3. 자료구조
 - graph : int[][]
 - visited : int[][]
 - queue : bfs

"""
from collections import deque

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().strip())))
visited = [[0] * M for _ in range(N)]
q = deque()
direction = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(x,y):
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y]
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
print(bfs(0,0))