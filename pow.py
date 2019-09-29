n = float(input())
n2 = int(input())

if n % 2 == 0:
    p = (n**2)**(n2/2)
else:
    p = n * (n**(n-1))

print(p)
