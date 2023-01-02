"""
빨간구슬 하나 파란구슬 하나
빨간구슬 구멍으로 빼내기
상하좌우 이동
빨간 구슬 구멍 성공
파란 구슬 구멍 실패
빨파 동시에 구멍 실패
빨파 같은 칸에 있을 수 없음
10번 이하로 움직이기 빼낼 수 없으면 -1 출력

1. 아이디어
 - 2 중 FOR문 => 빈칸 이동 구멍찾기
 - 최소 횟수 구하기 ,10번 초과로 움직일 경우 -1 출력

2. 시간복잡도
 - O(V+E)
 - V : 10 * 10
 - E : 4V
3. 자료구조
 - Graph int[][]
 - queue

"""
from collections import deque

N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(str,input().strip())))
direction = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            bx,by = i,j
        elif board[i][j] == 'R':
            rx,ry = i,j

"""
빨간구슬 구멍으로 빼내기
상하좌우 이동


빨파 동시에 구멍 실패
빨파 같은 칸에 있을 수 없음

"""
q = deque()
visited = [[[[False]*M for _ in range(N)]for _ in range(M)] for _ in range(N)]

def visit(x,y,dir):
    res = 0
    while board[x + direction[dir][0]][y + direction[dir][1]] != '#' and board[x][y] != 'O':
        #x,y = nx,ny
        x += direction[dir][0]
        y += direction[dir][1]
        res += 1
    return x,y,res

def bfs():
    q.append([rx,ry,bx,by,1])
    visited[rx][ry][bx][by] = True
    while q:
        nrx,nry,nbx,nby,cnt = q.popleft()
        if cnt > 10:
            print(-1)
            return
        for dir in range(4):
            nnrx,nnry,rres = visit(nrx,nry,dir)
            nnbx,nnby,bres = visit(nbx,nby,dir)
            if board[nnbx][nnby] == 'O':
                continue
            if board[nnrx][nnry] == 'O':
                print(cnt)
                return
            if nnrx == nnbx and nnry == nnby:
                if rres > bres:
                    nnrx -= direction[dir][0]
                    nnry -= direction[dir][1]
                else:
                    nnbx -= direction[dir][0]
                    nnby -= direction[dir][1]

            if not visited[nnrx][nnry][nnbx][nnby]:
                q.append([nnrx,nnry,nnbx,nnby,cnt + 1])
                visited[nnrx][nnry][nnbx][nnby] = True
    print(-1)
bfs()
