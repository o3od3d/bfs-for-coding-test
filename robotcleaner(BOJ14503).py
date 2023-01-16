"""
청소하는 영역의 개수 구하기
NXM크기 벽,빈칸으로 구성
청소기 바로보는 방향 있으며, 동서남북 중 하나이다.
작송
1. 현재 위치 청소
2. 현재 위치에서 현재 방향 기준으로 왼쪽방향부터 탐색
    1. 왼쪽 방향 아직 청소 X 그 방향으로 회전하고 한칸 전진하고 1부터 시작
    2. 왼쪽 청소할 공간 없으면, 그 방향으로 회전하고 2번으로 돌아감
    3. 네 방향모두 청소되어 있거나 벽인 경우, 바라보는 방향 유지하고 후진해서 2번으로 돌아감
    4. 네 방향모두 이미 청소되어 있고 벽이고 후진할 수 없으면 작동 멈춤
청소기는 이미 청소칸, 벽 통과 불가

1. 아이디어
 - 2중 FOR문 => 청소X(방문X) & 벽X
 - 청소한 칸의 개수 출력
2. 시간복잡도
 - O(N X M)

3. 자료구조
 - 그래프 :INT[][]
 - 방문 : BOOL[][]

"""
N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 1
board[r][c] = 2
direction = [[-1,0],[0,1],[1,0],[0,-1]]



# 2 현재 방향 기준 왼쪽 탐색
def exploration(x,y,tmp_d):
    global ans
    while True:
        for _ in range(4):
            tmp_d = (tmp_d + 3) % 4
            nx = x + direction[tmp_d][0]
            ny = y + direction[tmp_d][1]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    ans += 1
                    board[nx][ny] = 2
                    return [nx,ny,tmp_d]
        # 후진
        #tmp_d = (tmp_d + 2) % 4
        nx = x - direction[tmp_d][0]
        ny = y - direction[tmp_d][1]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 1:
            x,y = nx,ny
        else:
            return None

while True:
    res = exploration(r,c,d)
    if res == None:
        print(ans)
        break

    r,c,d = res

