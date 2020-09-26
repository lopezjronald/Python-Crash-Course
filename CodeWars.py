sum = 0
n = 4183059834009

x = float(4183059834009)
count = 1
while (x >= 1 or float(x**2) != n):
    x = (x/3)/count
    count += 1
    print(x)
print(x)