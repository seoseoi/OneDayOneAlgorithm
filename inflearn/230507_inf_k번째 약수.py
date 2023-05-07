n, k = map(int, input().split())

num = []
for i in range(1, n+1):
    if n%i == 0:
        num.append(i)
    else:
        pass

num.sort()

if len(num) < k:
    print(0)
else:
    ans = num[k-1]
    print(ans)

'''
answer

1. 리스트에 안 담고 바로 판단
2. 횟수를 변수 cnt 사용해 세기
3. for의 else
'''

n, k = map(int, input().split())

num = []
cnt = 0

for i in range(1, n+1):
    if n%i == 0:
        num.append(i)
        cnt += 1
    if cnt == k:
        print(i)
        break

else:
    print(0)