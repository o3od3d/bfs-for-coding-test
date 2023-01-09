"""
0은 바다
각 칸의 빙산은 바닷물에 접한 칸의 수만큼 줄어든다
0보다 낮아지지 않는다.
한 덩어리의 빙산이 두 덩어리 이상으로 분리되는 최소 시간?
두 덩어리 이상으로 분리되지 않으면 0 출력

1.아이디어
 - 2 중 for문 => 0아닌 것 주변 0 갯수 세어 빙산 줄이기
 - 덩어리 갯수 세기

2. 시간복잡도
 - O(V+E) < 2억 가능
 -V : 300 * 300
 - E : 4V

3. 자료구조
 - 그래프 : INT[][]
 - QUEUE : 덩어리 갯수

"""
import copy
from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
direction = [[0,1],[0,-1],[1,0],[-1,0]]
ans = 0

def bfs(x,y,tag):
    q = deque()
    q.append([x,y])
    tmp = copy.deepcopy(board)
    flag = 0
    while q:
        x,y = q.popleft()
        if board[x][y] > 0:
            flag = 1
            cnt = 0
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < M:
                if board[x][y] > 0 and board[nx][ny] == 0 and tag == 1:
                    tmp[x][y] -= 1
                    if tmp[x][y] < 0:
                        tmp[x][y] = 0
                if board[nx][ny] > 0 and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = True
    return flag,tmp

while True:

    ans += 1


    # 덩어리 갯수 구하기
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                flag,tmp = bfs(i,j,cnt)
                if cnt == 1:
                    board = tmp
                    if flag == 0:
                        print(0)
                        exit()



    if cnt > 1:
        print(ans)
        break
