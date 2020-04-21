n = -999
l = []
quantity = 0
while int(n) != 0:
    n = input()
    l.append(int(n))
m = max(l)
for i in l:
    if i == m:
        quantity += 1
print(quantity)
