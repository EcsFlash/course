n = int(input())
x = 1
s = 0
sum = 0
while x <= n:
    s = x ** 2
    x = x + 1
    sum = sum + s
print(sum)
