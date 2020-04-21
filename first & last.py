s = input()
c = len(s) - len(s.replace('f', ''))
if c == 0:
    pass
elif c == 1:
    print(s.index('f'))
else:
    print(s.index('f'), s.rindex('f'))
