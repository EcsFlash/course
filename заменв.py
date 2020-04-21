s = input()
for i in range(len(s)):
    if s[i] == "1":
        s = s.replace('1', 'one')
print(*s)
