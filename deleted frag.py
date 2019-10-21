s = input()
i = 0
while i < len(s):
    if s[i] == '@':
        s = s.replace('@', '')
    i += 1
print(s)
