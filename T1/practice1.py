#write a programe to calcluate eletricicty bill accept the no. of units from user;.

'''print("Welcome to Calcluate Your Bill")
units = int(input("Enter The Units : "))

if units <= 100:
    print("Your bill is Zero")
    amount = 0
elif units > 100 and units <= 200:
    amount = (units-100)*5
elif units >200 :
    amount = (units-200)*10 + (100*5)
print("Amount to Pay = ",amount)'''


#WAP TO check weather the enter no. is three digit No. or not , if it is then display the middle digit 

'''num = int(input("Enter No : "))
l = 0
for i in str(num):
    l+=1

if l == 3:
    print("Middle digit is : ",(num%100)//10)
else:
    print("Length of entered no is : ",l)'''

#WAP to accept the age , gender and no of days and display the wages according to the table , if does not in any range then display enter appropriate age.

'''age = int(input("Enter Age : "))
gen = str(input("Enter Gender : "))
nd = int(input("Enter No of days : "))

if age >= 18 and age < 30:
    if gen == "m" and "M":
        wage = 700
        final_wage = nd * 700
        print("Final wage is : ",final_wage)
    elif gen == "f" and "F":
        wage = 750
        final_wage = nd * 750
        print("Final wage is : ",final_wage)
    else:
        print("invailid gender form")
elif age >= 30 and age < 40:
    if gen == "m" and "M":
        wage = 800
        final_wage = nd * 800
        print("Final wage is : ",final_wage)
    elif gen == "f" and "F":
        wage = 850
        final_wage = nd * 850
        print("Final wage is : ",final_wage)
    else:
        print("invailid gender form")
else:
    print("Invailid Age !!") '''

#WAP to find sum of 10 no. and also find the Avg.

'''sum = 0
for i in range(1,11):
    num = int(input("Enter No : "))
    sum += num
print("Sum of 10 no. is : ",sum)
print("Avg of no is :", sum//10)'''

#WAP to enter three No. an check how many no. is available bt first two no. that are divisible ny third no.

'''num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
count = 0

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1, num2 + 1):
    if i % num3 == 0:
        count += 1

print("Numbers between ",num1," and ",num2," that are divisible by ",num3," : ",count)'''

#WAP to print multification table accept the no. of user to be printed.

'''num = int(input("Enter No : "))
for i in range(1,11):
    print(num , "*", i ,"=" , num*i)'''

#WAP to find factorial of an no. entered by number.

'''num = int(input("Enter NO : "))
fact = 1
if num == 0 or num == 1:
    print("Factorial of given no is = 1")
elif num < 0:
    print("Enter vailid number")
else:
    for i in range(2,num+1):
        fact = fact * i
    print("Factorial of given no is = ",fact)'''

#WAP to display fibonaci Seqeauce upto n term.

'''num = int(input("Enter no : "))
a = 0
b = 1

if num == 0:
    print("Enter a non zero Number .")

else:
    print("\nYour fibonaci series --->")
    for i in range(num):
        print(a,end=" ")
        a, b = b, a + b '''

#WAP to take ten no from user then print sum and avg.

'''sum = 0
ecount = 0
ocount = 0
for i in range(1,11):
    num = int(input("Enter No : "))
    if num % 2 == 0:
        sum += num
        ecount+=1
    elif num % 2 != 0:
        sum += num
        ocount+=1
    sum += num  

print("Sum of 10 no. is : ",sum)
print("Avg of no is :", sum//10)
print("Total even no :",ecount, "and Total odd no : ",ocount)
print("Sum of even no is : ",sum)
print("Sum of odd no is : ",sum)'''

#WAP to reverse a number by entered user.

'''num = int(input("Enter a number : "))
num1 = num
while num1 != 0:
    rem = num1 % 10
    num1 = num1 // 10
    print(rem,end="")

if num1 == num:
    print("\nThis number is palindrome.")
else:
    print("\nThis number is not palindrome.")'''
