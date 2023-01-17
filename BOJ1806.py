"""
1. 아이디어
 - 연속된다.
 - N 수들의 부분합 중 합이 s이상 되는 것 중 가장 짧은 길이


"""
N,S = map(int,input().split())
arr = list(map(int,input().split()))
minNum = 1e9
left,right = 0,0
tmp = arr[0]
while True:

    if tmp >= S:
        minNum = min(minNum,abs(right-left)+1)
        tmp -= arr[left]
        left += 1
    else:
        right += 1
        if right == N:
            break
        tmp += arr[right]


if minNum == 1e9:
    print(0)
else:
    print(minNum)