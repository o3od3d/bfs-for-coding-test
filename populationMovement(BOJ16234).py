"""
각 땅에는 나라가 하나씩 존재
a[r][c]명이 살고 있다 인접한 나라 사이에는 국경선 존재
인구 이동 없을 때까지 반복
 국경선 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면,
 두나라가 공유하는 국경선을 오늘 하루동안 연다
 위의 조건에 의해 국경선 열렸으면, 인구 이동 시작
 국경선 열려있어 인접한 칸만을 이용해 이동하며, 그 나라를 오늘 하루동안 연합이라 한다.
 연합 이루고 있는 각 칸의 인구수는 연합 인구수/연합이룬 칸 수 (소수점 버림
 연합 해체 국경 닫는다.
인구 이동 며칠 일어나는지

1. 아이디어
 - 2 중 FOR문 =>

"""
from collections import deque
N,L,R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

direction = [[0,1],[0,-1],[1,0],[-1,0]]
ans = 0

# 국경선 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면,
#  두나라가 공유하는 국경선을 오늘 하루동안 연다
def bfs(a,b):
    q = deque()
    q.append([a, b])
    result = []
    result.append([a, b])
    while q:
        x,y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < N:
                    tmp = abs(board[x][y] - board[nx][ny])
                    if L <= tmp <= R and not visited[nx][ny]:
                        result.append([nx,ny])
                        q.append([nx,ny])
                        visited[nx][ny] = True

    return result

while True:
    flag = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                result = bfs(i,j)
                if len(result) > 1:
                    flag = 1
                    number = sum([board[x][y] for x, y in result]) // len(result)
                    for x, y in result:
                        board[x][y] = number
    if flag == 0:
        break
    ans += 1
    # 연합 찾기

    # 연합 이루고 있는 각 칸의 인구수는 연합 인구수/연합이룬 칸 수 (소수점 버림
    #  연합 해체 국경 닫는다.
print(ans)
