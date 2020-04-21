n1 = input()
n2 = input()
n3 = input()
if n1 == n2 == n3:
    print('3')
elif n1 == n3 or n1 == n2 or n2 == n3:
    print('2')
if n1 != n3 and n1 != n2 and n2 != n3:
    print('0')
