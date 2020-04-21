a = int(input())
b = int(input())
n = int(input())
c1 = a * n
c2 = b * n
if c2 >= 100:
    c3 = c2 // 100
    c1 = c1 + c3
    c2 = c2 % 100
print(str(c1)+" "+str(c2))
