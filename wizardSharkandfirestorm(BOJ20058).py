"""

1. 아이디어

2. 시간복잡도

3. 자료구조

3 1
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
2
"""
import copy
from collections import deque
N,Q = map(int,input().split())
N = 2**N
board = [list(map(int,input().split())) for _ in range(N)]
L = list(map(int,input().split()))
direction = [[0,1],[0,-1],[1,0],[-1,0]]

def rotation90(l):
    tmp = copy.deepcopy(board)
    for n in range(0,N,l):
        num = 0
        for m in range(0, N, l):
            for i in range(n,n+l):
                for j in range(m,m+l):
                    tmp[i][j] = board[m+n+l-1-j][num]
                num += 1
    return tmp

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] > 0 and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

for q in range(Q):
    l = 2 ** L[q]
    # 90도 회전
    board = rotation90(l)
    # 얼음 -1
    tmp = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            cnt = 0
            if board[i][j] > 0:
                for dir in direction:
                    nx = i + dir[0]
                    ny = j + dir[1]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
                        cnt += 1
                if cnt < 3:
                    tmp[i][j] -= 1
    board = tmp
# 남아있는 얼음의 합
ans = 0
for b in board:
    ans += sum(b)
# 가장 큰 덩어리가 차지하는 칸의 개수
result = -1e9
visited = [[False] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if board[x][y] > 0 and not visited[x][y]:
            result = max(result,bfs(x,y))
print(ans)
if result == -1e9:
    print(0)
else:
    print(result)
