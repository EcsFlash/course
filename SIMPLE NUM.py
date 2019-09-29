n = input()


def IsPrime(n):
    i = len(n)
    if i == 1:
        return True
    else:
        return False


if IsPrime(n) == True:
    print('YES')
else:
    print('NO')
