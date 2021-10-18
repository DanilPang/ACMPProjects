a = int(input())
sum = 0
if a > 0 and a != 0:
    for i in range(1, a + 1):
        sum += i
else:
    for i in range(a, 2):
        sum += i

print(int(sum))