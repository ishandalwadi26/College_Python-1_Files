print(bin(15))
# for any base to binary.

print(oct(122))
# for octal !!

print(hex(122))
# for hexadecimal !! 
print()
print()

# ----------------------------------------------------------------

a = 12e4 
print(a)
print(type(a))
# if there is in any variables if e is accur then its denotes as a float Type.
print('-------------------------------------------------')

# ----------------------------------------------------------------
# for list
l = [1,2,3,4,5]
print(l)
print(l[0])
l[0] = 6
print(l)
print('-----------------------------------------------')

# for tuple
t = (1,2,3,4,5)
print(t)
print(t[0])
# t[0] = 6 not changable.
print(t)
print('-------------------------------------------------')

# for range
for i in range(-5,5):
    print(i)
print()

for i in range(5):
    print(i)
print()

for i in range(-5,5,2): 
    print(i)
print()
# output : -5,-3,-1,1,3
# first denotes starting , second denotes and , and the third one is called steps (by defult size is 1).
print('-------------------------------------------------')

# for mappig type dict
d = {10:"ishan" , 20:"ishanni", 10:"ishaan"}
print(d)
print(d[10])
print(d[20])
d[20] = "we rhe"
print(d)
print()
print('-------------------------------------------------')


# for Set type
s = {"ab","cd","ef","ab"}
print(s)
print()
print('-------------------------------------------------')

# for boolean type
print(20>3)
print(3>20)
print(20==2)
print(bool("abc"))
print(bool(""))
print(bool(120))
print(bool(0))
print()
print('-------------------------------------------------')

a,b,c = "rth","t i5u","ygr"
print(a)
print(type(a))
print()

# consider as typle
a = "rth","t i5u","ygr","rth"
print(a)
print(a[2])
print(type(a))
print()
print('-------------------------------------------------')

# -----------------------------------------------------------------------------
a = "ishan"
def chek():
    a = "ishanni"
    print(a)
chek()
print(a)
print()

a = "ishan"
def chek():
    global a
    a = "ishanni" 
    print(a)
chek()
print(a)
print()
print('-------------------------------------------------') 

'''uiwrwiurhiwu hriuw 
 yr4yr4 rr
  ry4ry8y r''' # for mulitiline Comments.

#------------------------------------------------------------------------
# Reading Inputs from usres.
a = input("Enter a Numer : ")
print("Your Number is --> "+a)
print(type(a))
print()
print('-------------------------------------------------') 

a = int(input("Enter First Numer : "))
b = int(input("Enter Second Numer : "))
print(a+b)
print(type(a),type(b))
print()
print('-------------------------------------------------') 

# Tpye Casting
# int() : converts to integer
print(int(12345))
print(int(True))
print(int(False))
print(int("104"))
# print(int("10.5")) GIves error
# print(int("ten")) gives error
# print(int("0B111")) gives error
print(int(0B11))
print()
print('-------------------------------------------------')

# Float() : converts to Float
print(float(12345))
print(float(True))
print(float(False))
print(float("10.5"))
# print(float("ten")) gives error
# print(float("0B11")) gives error
print(float(0B11))
print()
print('-------------------------------------------------')

# Boolean() : converts to Boolean
print(bool(0))
print(bool(1))
print(bool(0.123))
print(bool(0.0))
print(bool("True")) 
print(bool("False")) 
print(bool(""))
print()
print('-------------------------------------------------')

# str() : converts to str
print(str(10))
print(str(10.5))
print(str(True))
print()
print('-------------------------------------------------')

# -------------------------------------------------------------------------
# conversation set,tuple,list.
a = [1,2,3,4,5,3,2,5,4,1]
print(a)
print(type(a))
b = set(a)
print(type(b))
print(b)
print()
print('-------------------------------------------------')

# Arthmatic Oprators
# 1. Addition : a + b
# 2. Subtraction : a - b
# 3. Multiplication : a * b
# 4. Division : a / b
# 5. Modulus : a % b
# 6. Exponentiation : a ** b
# 6. Floor divisoin : a // b   # Floor Division has higher precedence than Normal Division and it also rounds off to the nearest floor value in int.
                               # So it is better to use floor division than converting a value to int and then rounding it off to the nearest smallest value. 
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)
print(10 // 5)
print()
print('-------------------------------------------------')
