"""
1. 아이디어
 - 0이 아닌 칸 찾기 - 주변의 0 갯수 세기
 - 2 중 for 문 => 값 0x && 방문x
 - 덩어리 찾기
2. 시간복잡도
 - O(V+E) < 2억
 - V : 300 * 300
 - E: 4V

3. 자료구조
 - 그래프 : INT[][]
 - QUEUE
 - 방문 : BOOL[][]
"""
from collections import deque
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
direction = [[0,1],[0,-1],[1,0],[-1,0]]

# 빙하 위치 담기
ice = []
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            ice.append((i,j))

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    res = []
    while q:
        x,y = q.popleft()
        cnt = 0
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    cnt += 1
                elif not visited[nx][ny] and board[nx][ny] > 0:
                    q.append([nx,ny])
                    visited[nx][ny] = True
        if cnt > 0:
            res.append([x,y,cnt])
    for x,y,cnt in res:
        board[x][y] = max(0,board[x][y]-cnt)
    return 1
times = 0
while True:

    mass = 0
    visited = [[False] * M for _ in range(N)]
    tmp = []
    for i,j in ice:
        if not visited[i][j] and board[i][j]:
            mass += bfs(i,j)
        if board[i][j] == 0:
            tmp.append((i,j))
            # 빙하 녹이기

    # 끝내기
    if mass > 1:
        print(times)
        break
    ice = sorted(list(set(ice) - set(tmp)))
    if len(ice) == 0:
        print(0)
        break
    times += 1


