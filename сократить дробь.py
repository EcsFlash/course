from math import gcd
n = int(input())
n2 = int(input())


def rf(n, n2):
    d = gcd(n, n2)
    return (n//d, n2//d)


print(rf(n, n2))
