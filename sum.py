n = int(input())
n2 = int(input())


def s(n, n2):
    return s(n+1, n2-1) if n2 > 0 else n


print(s(n,n2))
