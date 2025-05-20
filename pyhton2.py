n = 10
a = 0
b = 1
c = 12
d = 23
next = b  
count = 1

while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()
