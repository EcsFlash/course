n = int(input())
cn = n
quantity = 0
max_quantity = 0
while n != 0:
    if cn == n:
        quantity += 1
    else:
        if quantity > max_quantity:
            max_quantity = quantity
        quantity = 1
        cn = n
    n = int(input())
print(max(quantity,max_quantity))
