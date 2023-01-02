"""
1. 아이디어
 - 고슴도치 물, 돌 피해 굴로 이동하기
 - 최소 시간, 이동 불가 KAKTUS

2. 시간 복잡도
 - O(2V+E)
 - V : 50 * 50
 - E : 4V

3. 자료구조
 - GRAPH : str[][]
 - queue

"""
from collections import deque
R,C = map(int,input().split())
graph = []
for _ in range(R):
    graph.append(list(map(str,input().strip())))
direction = [[0,1],[0,-1],[1,0],[-1,0]]
visitedDochi = [[0] * C for _ in range(R)]
q = deque()
ex,ey = 0,0

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            q.append([i,j])
        elif graph[i][j] == 'D':
            ex,ey = i,j
for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        if graph[ex][ey] == 'S':
            return visitedDochi[ex][ey]
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < R and 0 <= ny < C:

                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    q.append([nx,ny])
                    visitedDochi[nx][ny] = visitedDochi[x][y] + 1
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append([nx,ny])
    return 'KAKTUS'

print(bfs())
