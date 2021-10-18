n = int(input())
arr = [int(i) for i in input().split()]
arr = arr[:n]
minn = min(arr)
maxn = max(arr)
div = 1
sum = 0

for i in range(n):
    if arr[i] == maxn:
        maxnIndex = i
    if arr[i] == minn:
        minnIndex = i
    if arr[i] > 0:
        sum += arr[i]

if minnIndex > maxnIndex:
    for i in range(maxnIndex + 1, minnIndex):
        div *= arr[i]
else:
    for i in range(minnIndex + 1, maxnIndex):
        div *= arr[i]

print(div, sum)