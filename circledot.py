x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
rightborder = xc + r
leftborder = xc - r
borderdown = yc - r
borderup = yc + r


def IsPointInCircle(x, y, rightborder, leftborder, borderdown, borderup):
    return y <= borderup and x <= rightborder and y >= borderdown and x >= leftborder

g = IsPointInCircle(x, y, rightborder, leftborder, borderdown, borderup)
if g == True:
    print('YES')
else:
    print('NO')
