a = int(input())
b = int(input())
c = int(input())
A = int(input())
B = int(input())
C = int(input())
v1 = a * b * c
v2 = A * B * C
if v1 == v2:
    print("Boxes are equal")
elif v1 > v2:
    print('The first box is larger than the second one')
elif v2 > v1:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
