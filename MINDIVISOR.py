n = int(input())
from math import sqrt
mind = 2


def MinDivisor(n, mind):
    while mind <= sqrt(n):
        while n % mind != 0:
            mind += 1
    return mind


print(MinDivisor(n, mind))
