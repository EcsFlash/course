n = -1
max = 0
quantity = 0
while n != 0:
    n = int(input())
    if n > max:
        max = n
        quantity = 1
    elif n == max:
        quantity += 1
print(quantity)
