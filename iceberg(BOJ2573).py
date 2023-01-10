"""
각 빙산에 상하좌우에 붙어 있는 0 개수만큼 빙산의 크기가 줄어든다.
단, 0 이하로 내려갈 수 없다.
하나의 덩어리가 2개 이상의 덩어리로 분리될 때까지 몇년이 걸리는지 분리되지 않으면 0

1. 아이디어
 - 2 중 for문 : 0의 갯수만큼 빼주기(마지막에) & 방문 x
 - 덩어리 개수 확인

2. 시간복잡도
 - O(V+E)
 - V : 300 * 300
 - E : 4V

3. 자료구조
 - 그래프 : int[][]
 - 방문 : bool[][]

"""
import sys
input = sys.stdin.readline
from collections import deque


def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    sea = []
    while q:
        x,y = q.popleft()
        cnt = 0
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < M:
                if not board[nx][ny]:
                    cnt += 1
                elif board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
        if cnt > 0:
            sea.append((x,y,cnt))
    for x,y,cnt in sea:
        board[x][y] = max(0,board[x][y] - cnt)
    return 1

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
direction = [[0,1],[0,-1],[1,0],[-1,0]]
ice = []
for i in range(N):
    for j in range(M):
        if board[i][j]:
            ice.append((i,j))


while True:
    res = []
    visited = [[0] * M for _ in range(N)]
    group = 0
    for i,j in ice:
        if board[i][j] and not visited[i][j]:
            group += bfs(i,j)
        if board[i][j] == 0:
            res.append((i,j))
    if group > 1:
        print(ans)
        break
    ice = sorted(list(set(ice) - set(res)))
    ans += 1

if group < 2:
    print(0)
