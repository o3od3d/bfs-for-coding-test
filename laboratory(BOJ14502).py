"""
1. 아이디어
 - 2 중 for문 => 벽 3개를 이용하여 바이러스가 최대한 적게 퍼지도록
 - 안전 영역 최대 크기

2. 시간복잡도
 - O(V+E)
 - V : 8 * 8
 - E : 4V

3. 자료구조
 - graph
 - visited
 - queue
 - 벽 놓기
"""
# 0 빈칸 1 벽 2 바이러스
import copy
from itertools import combinations
from collections import deque
N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
direction = [[0,1],[0,-1],[1,0],[-1,0]]
ans = 0
virus = []
# 바이러스 담기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append([i,j])
q = deque()
def bfs(graph):
    copy_graph = copy.deepcopy(graph)
    for x,y in virus:
        q.append([x,y])
    while q:
        vx,vy = q.popleft()
        for dir in direction:
            nx = vx + dir[0]
            ny = vy + dir[1]
            if 0 <= nx < N and 0 <= ny < M:
                if copy_graph[nx][ny] == 0:
                    q.append([nx,ny])
                    copy_graph[nx][ny] = 2
    res = 0
    for g in copy_graph:
        res += g.count(0)
    return res


def wall(cnt,graph):
    global ans
    if cnt == 3:
        ans = max(ans,bfs(graph))
    else:
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    cnt += 1
                    graph[i][j] = 1
                    wall(cnt,graph)
                    cnt -= 1
                    graph[i][j] = 0
wall(0,graph)
print(ans)
"""
# 빈칸위치
empty = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty.append([i,j])

def bfs():
    ans = 0
    for com in combinations(empty,3):
        copy_graph = copy.deepcopy(graph)
        for x,y in com:
            copy_graph[x][y] = 1
        q = deque()
        # 바이러스 담기
        for i in range(N):
            for j in range(M):
                if copy_graph[i][j] == 2:
                    q.append([i,j])
        while q:
            vx,vy = q.popleft()
            for dir in direction:
                nvx = vx + dir[0]
                nvy = vy + dir[1]
                if 0 <= nvx < N and 0 <= nvy < M:
                    if copy_graph[nvx][nvy] == 0:
                        copy_graph[nvx][nvy] = 2
                        q.append([nvx,nvy])
        res = 0
        for g in copy_graph:
            res += g.count(0)
        ans = max(ans,res)
    return ans"""