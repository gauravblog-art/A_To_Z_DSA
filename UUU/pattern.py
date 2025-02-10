n=int(input())

print(n)
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
    for j in range(n*2-1-i*2):
        print("*", end="")
    print()

print("===========")

k=1
for i in range(n):
    for j in range(i+1):
        print(k, end=" ")
        k+=1
    print()

print("=============")

def numtochr(num):
    return chr(num+65)

for i in range(n):
    for j in range(i+1):
        print(numtochr(j), end="")
    print()

print("=============")
# ABCDE
# ABCD
# ABC
# AB
# A
for i in range(n):
    for j in range(n-i):
        print(numtochr(j), end="")
    print()
print("=========")
# A
# BB
# CCC
# DDDD
# EEEEE
for i in range(n):
    for j in range(i+1):
        print(numtochr(i), end="")
    print()

print("===========")
#    A
#   ABA
#  ABCBA
# ABCDCBA
for i in range(n-1):
    for j in range(n-i-2):
        print(" ", end="")
    for j in range(i+1):
        print(numtochr(j), end="")
    for k in range(i-1, -1, -1):
        print(numtochr(k), end="")
    print()

print("===============")
# E
# DE
# CDE
# BCDE
# ABCDE
k=n-1
for i in range(n):
    for j in range(i+1):
        print(numtochr(k+j), end="")
    k-=1
    print()

print("=================")
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
for i in range(n):
    
    for j in range(n-i):
        print("*", end="")
    for j in range(i):
        print(" ", end=" ")
    for j in range(n-i):
        print("*", end="")
    print()

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end="")
    print()
print("================")
for i in range(2*n):
    if i<n:
        for j in range(n-i):
            print("*", end="")
        for j in range(i):
            print(" ", end=" ")
        for j in range(n-i):
            print("*", end="")
        print()
    
    elif i>=n:
        for j in range(i-n+1):
            print("*", end="")
    
        for j in range(2*n-i-1):
            print(" ", end=" ")
        for j in range(i-n+1):
            print("*", end="")
        print()



