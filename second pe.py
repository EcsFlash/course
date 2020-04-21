s = input()
c = 0
for i in range(len(s)):
    if s[i] == "f":
        c += 1
        if c == 2:
            print(i)

if c == 1:
        print('-1')
elif "f" not in s:
    print('-2')
