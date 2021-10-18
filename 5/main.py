n = int(input())
arr = [int(i) for i in input().split()]
arr = arr[:n]
count3, count4 = 0, 0

for i in range(n):
    if arr[i] % 2 != 0:
        print(arr[i], end=' ')
        count3 += 1

print()

for i in range(n):
    if arr[i] % 2 == 0:
        print(arr[i], end=' ')
        count4 += 1

if count4 >= count3:
    print('\nYES')
else:
    print('\nNO')