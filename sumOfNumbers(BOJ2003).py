"""
1. 아이디어
 - 처음에 2개 값 더한다.
 - 주어진 값보다 작은 경우 하나 더해주고
 - 주어진 값보다 큰 경우 하나 빼준다.
 - 주어진 값과 같은 경우 cnt++
2. 시간복잡도
 - O(N) = 10,000 < 2억

3. 자료구조
 - 숫자 배열 : int[]
 - 결과 합 : M * N = 300,000,000 < 20억
"""
N,M = map(int,input().split())
num = list(map(int,input().split()))
ans = 0
left,right = 0,1
while right <= N and left <= right:
    sumres = num[left:right]
    total = sum(sumres)
    if total == M:
        ans += 1
        right += 1
    elif total < M:
        right += 1
    else:
        left += 1
print(ans)