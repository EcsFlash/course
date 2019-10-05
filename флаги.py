n = int(input())
flag = ['+___ ',
        '|%s / ',
        '|__\ ',
        '|    ']
print(flag[0] * n)
for i in range(1, n + 1):
    print("|", i, " /", sep="", end=" ")
print()
print(flag[2] * n)
print(flag[3] * n)
