"""
인구수와 인접한 구역의 정보가 주어지고
2개의 선거구로 나누고 각 선거구의 인구수 차이를  최소로 하는 경우 출력
2개로 나눌 수 없을 경우 -1 출력

1. 아이디어
 - 다양한 탐색 위해 DFS 사용
2. 시간복잡도
 - O(V+E)

3. 자료구조
"""
import sys
sys.setrecursionlimit(10**7)
from collections import deque
N = int(input())
number = list(map(int,input().split()))
board = [[]]

for _ in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp[1:])

ans= 1e9
res = []

def bfs(q1,q2):
    res1,res2 = [],[]
    print('야',q1,q2)
    while q1:
        nx = q1.popleft()
        res2.append(nx)
        for i in board[nx]:
            res1.append(i)
    if res1 != res2:
        return -1
    res1, res2 = [], []
    while q2:
        nx = q2.popleft()
        res2.append(nx)
        for i in board[nx]:
            res1.append(i)
    if res1 != res:
        return -1
    return 1
def dfs(x,n):
    global ans
    if n == num:
        a,b = 0,0
        q1,q2 = deque(),deque()
        for r in res:
            a += number[r-1]
            q1.append(r)
        for j in range(1,N+1):
            if j not in res:
                b += number[j-1]
                q2.append(j)

        if bfs(q1,q2):
            ans = min(ans,abs(a-b))

    for i in board[x]:
        if i not in res and not visited[i]:
            visited[i] = True
            res.append(i)
            bfs(i,n+1)
            res.remove(i)
            visited[i] = False
res.append(1)
for num in range(1,N//2+1):
    visited = [False for _ in range(N+1)]
    dfs(1,1)
print(ans)