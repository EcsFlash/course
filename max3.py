n = -999
l = []
while int(n) != 0:
    n = input()
    l.append(int(n))
l.sort()
print(l[-2])
