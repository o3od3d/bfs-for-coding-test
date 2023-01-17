"""
1. 아이디어
 - 주어진 숫자 만큼 더하는 대신 소수만 가능
 - 소수판별,
 - 연속하므로 투포인터
 - 같으면 ans ++ right ++
 - 더 크면 left ++
 - 더 작음녀 right ++
"""
N = int(input())
ans = 0
left,right = 0,0
sumNum = 2

# 에라토스테네스의 체
a = [False,False] + [True] * (N+1)
for i in range(2,int(N**0.5)+1):
    if a[i]:
        for j in range(i*2,N+1,i):
            a[i] = False
prime = []
for i in range(2,N+1):
    if a[i]:
        prime.append(i)
print(prime)
while True:
    if sumNum <= N:
        if sumNum == N:
            ans += 1
        right += 1
        if right == len(prime):
            break
        sumNum += prime[right]
    else:
        sumNum -= prime[left]
        left += 1
print(ans)