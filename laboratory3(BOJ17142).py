"""
1. 아이디어
 - 2 중 for 문 => M개 바이러스 활성화
 - 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간

2. 시간 복잡도
 - O(V+E) = 5V = 5 * 2500 < 2억 가능!
 - V : 50 * 50
 - E : 4V

3. 자료 구조
 - 그래프 : INT[][]
 - 방문 : INT[][]
 - QUEUE : BFS

"""
import copy
from collections import deque
from itertools import combinations
N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
q = deque()
direction = [[0,1],[0,-1],[1,0],[-1,0]]
ans = 1e9
virus = []
wall = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i,j])
        elif board[i][j] == 1:
            wall += 1
def bfs():
    global ans
    for com in combinations(virus,M):
        visited = [[-1] * N for _ in range(N)]
        copy_b = copy.deepcopy(board)
        for x,y in com:
            q.append([x,y])
            visited[x][y] = 0
        res = 0
        while q:
            x,y = q.popleft()
            for dir in direction:
                nx = x + dir[0]
                ny = y + dir[1]
                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] == -1 and copy_b[nx][ny] != 1:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[x][y] + 1
                        if copy_b[nx][ny] == 0:
                            res = max(res,visited[nx][ny])
        cnt = 0
        for v in visited:
            cnt += v.count(-1)

        if cnt != wall:
            ans = min(ans,1e9)
        else:
            ans = min(ans,res)
    return ans
bfs()
if ans == 1e9:
    print(-1)
else:
    print(ans)