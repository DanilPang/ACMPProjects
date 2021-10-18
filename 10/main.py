a, b, c, d = input().split()

for x in range(-100, 101):
    if ((int(a) * (x**3)) + (int(b) * (x**2)) + (int(c) * x) + int(d)) == 0:
        print(x, end=' ')
