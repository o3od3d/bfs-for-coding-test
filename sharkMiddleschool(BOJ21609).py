"""
1. 아이디어
 - 블록 그룹 찾기 -1,0아닌 것 찾기
 - 2 중 for문 => 해당 숫자와 0 포함하는 블록 그룹 갯수(2개 이상)와 0갯수,기준 블록 위치
 - 1만족하는 블록 제거하고 점수 B^2 획득
 - 중력 작용
 - 90도 반시계 회전
 - 중력 작용
 - 그룹 없을 때까지 반복

2. 시간복잡도
 -  O(V+E)
 - V: 20 * 20 < 2억
 - E: 4V

3. 자료구조
 - 그래프 : INT[][]
 - QUEUE: BFS


"""
import copy
from collections import deque
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
direction = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    size = 1
    pos,rainbow = [],[]
    pos.append([x,y])
    while q:
        nx,ny = q.popleft()
        for dir in direction:
            nnx = nx + dir[0]
            nny = ny + dir[1]
            if 0 <= nnx < N and 0 <= nny <N:
                if (board[nnx][nny] == board[x][y] or board[nnx][nny] == 0) and not visited[nnx][nny]:
                    q.append((nnx,nny))
                    visited[nnx][nny] = True
                    size += 1
                    pos.append([nnx,nny])
                    if board[nnx][nny] == 0:
                        rainbow.append([nnx,nny])
    for x,y in rainbow:
        visited[x][y] = False
    return size,len(rainbow),pos

def gravity():
    for i in range(N-2,-1,-1):
        for j in range(N):
            if board[i][j] > -1:
                r = i
                while True:
                    if 0 <= r+1 < N and board[r+1][j] == -2:
                        board[r+1][j] = board[r][j]
                        board[r][j] = -2
                        r += 1
                    else:
                        break
def rotation90():
    tmp = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            tmp[i][j] = board[j][N-i-1]
    return tmp

while True:

    # 블록 그룹 찾기
    result = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                size,rainbow,pos = bfs(i,j)
                if size >=2 :
                    result.append([size,rainbow,pos])
    # 가장 크기 크고, 무지개 블록 수 많고, 기준 행 크고, 열 큰 것 제거
    if len(result) == 0:
        break
    #result = sorted(result,key=lambda x:(x[0],x[1],x[2],x[3]))
    result.sort(reverse=True)
    size, rainbow, pos = result.pop(0)
    for n,m in pos:
        board[n][m] = -2
    ans += (size**2)

    # 중력 작용
    gravity()
    # 90도 반시계 회전
    board = rotation90()
    # 중력 작용
    gravity()

print(ans)
