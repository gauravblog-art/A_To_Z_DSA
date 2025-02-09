n=5
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

print("=============")
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

print("==============")

for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

print("================")

for i in range(n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()

print("===========")

for i in range(n+1):
    for j in range(1, n+1-i):
        print(j, end="")
    print()

print("===============")

for i in range(1,n+1):
    for j in range(i):
        print (i, end="")
    print()

print("============")



for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range(i*2+1):
        print("*", end=" ")
    print()

print("===========")

for i in range(n):
    for k in range(i-1+1):
        print("", end=" ")
    for j in range(n*2-1-i*2):
        print("*", end="")
    print()
    
print("============")

for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range(i*2+1):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i-1+2):
        print("", end=" ")
    for j in range(n*2-1-i*2-1):
        print("*", end="")
    print()