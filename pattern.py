#WAP to create a pattern
n = int(input("enter no to create pattern : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()


n = int(input("\nenter no to create pattern : "))

for i in range(0,n+1):
    for j in range(i,n):
        print("* ",end="")
    print()

n = int(input("\nenter no to create number pattern : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

n = int(input("\nenter no to create number pattern : "))
k = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end="")
        k+=1
    print()

n = int(input("\nenter no to create number pattern : "))
k = 97
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(k),end="")
        k+=1
    print()


n = int(input("\nenter no to create number pattern : "))
k = 65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(k),end="")
        k+=1
    print()


n = int(input("\nenter no to create number pattern : "))
for i in range(1,n+1):
    k = 65
    for j in range(1,i+1):
        print(chr(k),end="")
        k+=1
    print()

n = int(input("\nenter no to create number pattern : "))
k = 65
num = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2 != 0:
            print(num,end="")
            num+=1
        else:
            print(chr(k),end="")
            k+=1
    print()

n = int(input("\nenter no to create number pattern : "))
k = 65
num = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2 == 0:
            print("#",end="")
            num+=1
        else:
            print("*",end="")
    print()

n = int(input("\nenter no to create number pattern : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2 == 0:
            print("1",end="")
            num+=1
        else:
            print("0",end="")
    print()

n = int(input("\nenter no to create reverse Full pyramid : "))

for i in range(n,0,-1):

    for j in range(i,n):
        print(" ",end="")

    for j in range(i):
        print("* ",end="")
    print()

n = int(input("\nenter no to create reverse Full pyramid : "))

for i in reversed(range(n,0,-1)):

    for j in range(i,n):
        print(" ",end="")

    for j in range(i):
        print("* ",end="")
    print()

n = int(input("\nenter no to create reverse Full pyramid : "))

for i in range(1,n+1):

    for j in range(1,n+1-i):
        print(" ",end="")

    for j in range(i):
        print("*",end="")
    print()
