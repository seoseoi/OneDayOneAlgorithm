import sys

n = int(sys.stdin.readline())

num = n * [0]
cnt = 0
for i in range(1, n):
    if num[i] == 0:
        cnt += 1
        for j in range(i, n, i+1):
            num[j] = 1

print(cnt)
