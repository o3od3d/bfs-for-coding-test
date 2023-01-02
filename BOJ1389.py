"""
1. 아이디어
 - 서로 연결된 사람 그래프로 표시
 - 케빈 베이컨 수 가장 작은 것 중 번호 가장 작은것

2. 시간복잡도
 - O(V+E)
 - V : 100
 - E : 5000

3. 자료구조
 - 그래프 : int[][]
 - queue

"""
from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
q = deque()


def bfs(x):
   cnt = [0] *(N+1)
   visited = [x]
   q.append(x)
   while q:
        x = q.popleft()
        for i in graph[x]:
            if i not in visited:
                cnt[i] = cnt[x] + 1
                visited.append(i)
                q.append(i)
   return sum(cnt)
minVal = 1e9
ans = 1e9
for x in range(1,N+1):
    res = bfs(x)

    if minVal > res:
        minVal = res
        ans = x
    elif minVal == res:
        ans = min(ans,x)
print(ans)