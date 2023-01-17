"""
두 배열합쳐서 정렬하는 프로그램
"""
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
left,right = 0,0
res = []
while True:
    if A[left] <= B[right]:
        res.append(A[left])
        left += 1
    elif A[left] > B[right]:
        res.append(B[right])
        right += 1
    if left == N:
        res.extend(B[right:])
        break
    elif right == M:
        res.extend(A[left:])
        break
print(' '.join(map(str,res)))