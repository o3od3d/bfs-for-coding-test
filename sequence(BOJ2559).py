"""
1. 아이디어
 - 처음에 K개 값을 구한다.
 - FOR 문을 이용해 다음값 더하고 앞의 값을 빼준다.
 - 이때마다 최대값을 갱신한다.

2. 시간복잡도
 - O(N) = 100,000 < 2 억

3. 자료구조
 - 전체 정수 : INT[]
 - 합한 수 : INT
    - num * K = 100 * 1e5 < 20억
"""
N,K = map(int,input().split())
number = list(map(int,input().split()))
ans = 0
for i in range(K):
    ans += number[i]
maxNum = ans
if N == K:
    print(ans)
else:
    for i in range(K,N):
        ans -= number[i-K]
        ans += number[i]
        if ans > maxNum:
            maxNum = ans
    print(maxNum)