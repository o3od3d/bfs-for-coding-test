"""
m명의 승객 태우기
상하좌우 빈칸 이동 최단경로
현 위치에서 최단 거리 가장 짧고 행 번호가장 작고 열번호 가장 작은 승객
같은 위치면 해당 거리 0
한 칸 이동 시 연로 1 소요
소모 연료량 두배 충전
이동 중 바닥나면 실패
1. 아이디어
 - 2 중 for문 => 최단경로 중 행 작고 열 작은 승객 찾기 빈칸 이동
 - 연료 소모량 계산 후, 현재 연료보다 크면 종료, 작거나 같으면2 배 충전
 - m명 다 태우면 종료하거나 연료 소모면 종료

2. 시간 복잡도
 - O(V+E) = 6V < 2억 가능
 - V : 20 * 20
 - E : 5V

3. 자료구조
 - 그래프 INT[][]
 - 방문여부
 - QUEUE

"""
from collections import deque
N,M,capacity = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
tx,ty = map(int,input().split())
tx -= 1
ty -= 1
start = []
end = []
for _ in range(M):
    cx,cy,ex,ey = map(int,input().split())
    start.append([cx-1,cy-1])
    end.append([ex-1,ey-1])
q = deque()
direction = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0
    res = []
    while q:
        x,y = q.popleft()
        if [x,y] in start:
            res.append([x,y,visited[x][y]])
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
    return sorted(res,key=lambda x:(-x[2],-x[0],-x[1]))

def des(x,y,ex,ey):
    q = deque()
    q.append([x,y])
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
            return visited[x][y]
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
    return -1

"""
한 칸 이동 시 연로 1 소요
소모 연료량 두배 충전
이동 중 바닥나면 실패
"""
while True:

    if len(start) == 0:
        break

    # 가장 거리 짧고 행 작고 열 작은 승객 찾기
    result = bfs(tx,ty)
    if len(result) == 0:
        capacity = -1
        break
    sx,sy,cap = result.pop()
    # 찾으러 가는 길에 연료 확인
    if cap >= capacity:
        capacity = -1
        break
    capacity -= cap
    # 택시 위치 갱신하고 승객 도착지로 이동
    tx,ty = sx,sy
    idx = start.index([sx,sy])
    start.pop(idx)
    cap = des(tx,ty,end[idx][0],end[idx][1])
    # 도착해서 연료 확인
    if cap > capacity or cap == -1:
        capacity = -1
        break
    tx,ty = end[idx][0],end[idx][1]
    capacity += cap
    end.pop(idx)
# 처리 왼료 시 삭제
# 종료조건
print(capacity)