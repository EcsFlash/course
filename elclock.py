n = int(input())
h = (n % 1440) // 60
min = (n % 1440) % 60
print(str(h)+" "+str(min))
