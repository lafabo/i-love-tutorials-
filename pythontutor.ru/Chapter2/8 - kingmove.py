a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (c == a - 1 or c == a + 1 or c == a) and (d == b - 1 or d == b + 1 or d == b):
    print("YES")
else:
    print("NO")