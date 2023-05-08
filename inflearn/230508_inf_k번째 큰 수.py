# 변수 정확히 쓸 것

n, k = map(int, input().split())
card = list(map(int, input().split()))

sum = []
for h in range(n):
    for i in range(h+1, n):
        for j in range(i+1, n):
            sum.append(card[h]+card[i]+card[j])

sum = set(sum)
sum = list(sum)
sum.sort()

print(sum[-k])