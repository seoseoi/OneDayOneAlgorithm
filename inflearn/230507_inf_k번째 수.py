import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for x in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    need = arr[i-1:j]
    need.sort()
    print(need[k-1])