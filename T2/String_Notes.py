# (1) Accesing Characters of String using Index :-

# s = "LJ University"

# print(s[1])
# print(s[-1])
# print(s[-5])
# print(s[25])

# ----------------------------------------------------------------------------------

# (2) Accesing Characters of String using Slicing operators :-
# Syntax of slicing operators :- s[beginIndex : endIndex : Step] 

# s = "Learning Python is very easy!!"

# print(s[1 : 7 : 1])
# print(s[1 : 7 : 2])
# print(s[1 : 7])
# print(s[:7])
# print(s[9:])
# print(s[::])
# print(s[:])
# print(s[::-1])
# print(s[-1 : -4]) # Note : By Default step is 1, so here (-1) + (+1) = (0) so it never goes to -4 and gives blank output
# print(s[-1 : -4 : -1]) # Solution of above case!

# ----------------------------------------------------------------------------------

# (3) Mathematical Operators for String :-
# + --> Concatenation
# * --> Repetition or String Multiplication

# print("Arman" + "Dhairya")
# print("Lucky" * 3)

# ----------------------------------------------------------------------------------

#  (4) Comparision of String :-

# s1 = input("Enter First String = ")
# s2 = input("Enter Second String = ")

# if (s1==s2):
#     print("Both Strings are Equal")
# elif (s1<s2):
#     print("First String is Smaller than Second String")
# else:
#     print("First String is Larger than Second String")

# ----------------------------------------------------------------------------------

# (5) Joining of String :-
# Syntax :- s = "separator".join(Group Of Strings)

# tuple = ("Apple", "Banana" , "Cherry")
# s = "-".join(tuple)
# print(s)

# ----------------------------------------------------------------------------------

# (6) Formatting of Strings :-

# name = "Arman"
# salary = 55000
# age = 25
# print("{}'s salary is {} and his age is {}".format(name,salary,age)) # Similar to f-String!
# print("{0}'s salary is {1} and his age is {2}".format(name,salary,age))
# print("{0}'s salary is {0} and his age is {0}".format(name,salary,age))
# print("{1}'s salary is {0} and his age is {2}".format(name,salary,age))
# print("{}'s salary is {} and his age is ".format(name,salary,age)) # Here an extra parameters will not give us error
# print("{}'s salary is {} and his age is {} and {}".format(name,salary,age)) # Although here it will give us an IndexError due to an extra {}

# ----------------------------------------------------------------------------------

# (7) Important Functions of String! :-

# (i) len() :- Calculates the Length of the String

# a = "LJ University!"
# print(len(a))

# ---------------------------------------------

# (ii) Removing Spaces from String :-
        
# (ii.i) rstrip() :- Removes Spaces from Right Side!

# t = "banana     "
# x = t.rstrip()
# print(len(t))
# print(len(x))

# t = "banana     "
# x = t.rstrip("a") # Here It Does not Removes A It's First Priority is to remove Spaces!
# print(x)

# t = "banana"
# x = t.rstrip("a") # Here It Removes "a" iterating from Right as there are no Spaces!
# print(x)

# t = "banana"
# x = t.rstrip("an") # Here It Removes "a & n" iterating from Right till it Reaches to end or any other character other than a and n!
# print(x)

# t = "bandana"
# x = t.rstrip("an") # Here It Does not Removes "a & n" till any other Character does not come!
# print(x)

# ---------------------------------------------

# (ii.ii) lstrip() :- Removes Spaces from Left Side!

# t = "     banana"
# x = t.lstrip()
# print(len(t))
# print(len(x))

# t = "bandana"
# x = t.lstrip("ban")
# print(x)

# t = "      banana      "
# x = t.lstrip("F")
# print(x)

# t = "    F  banana      "
# x = t.lstrip("F")
# print(x)

# ---------------------------------------------

# (ii.iii) strip() :- Removes Spaces from Both Sides!

# t = "       banana       "
# x = t.strip()
# print(len(t))
# print(len(x))
# print("From all Fruits",x,"is my Favourite")

# ---------------------------------------------

# (iii) upper() :- Converts the String to Upper-Case

# t = "Hello Friends"
# x = t.upper()
# print(x)

# ---------------------------------------------

# (iv) lower() :- Converts the String to Lower-Case

# t = "Hello Friends"
# x = t.lower()
# print(x)

# ---------------------------------------------

# (v) swapcase() :- Converts Upper-Case Characters to Lower-Case and vice-versa

# t = "Hello my name is TEJAS"
# x = t.swapcase()
# print(x)

# ---------------------------------------------

# (vi) title() :- All the First characters of each word is Upper-Case and rest all are Lower-Case
                # It will check only for Alphabets

# t = "Welcome to LJIET"
# x = t.title()
# print(x)

# ---------------------------------------------

# (vii) capitalize() :- The First Character is in Upper-Case and rest of the STRING is in Lower-Case

# t = "Learning Python is very easy!"
# x = t.capitalize()
# print(x)

# ---------------------------------------------

# (viii) isalnum() :- To check type of characters present in a String(Check Function)
                    # Answer only in True or False
                    # (a to z, A to Z, 0 to 9)

# t = "Tejas 123"
# print(t.isalnum())

# t = "Company123"
# print(t.isalnum())

# ---------------------------------------------

# (viii) isaplha() :- Answer only in True or False
                    # (a to z, A to Z)
                    # Returns True if all characters are Alphabet Symbols

# t = "Tejascsd"

# ---------------------------------------------

# (ix) isdigit() :- Works for Digits

# t = "500000"
# print(t.isdigit())

# ---------------------------------------------

# (x) isnumeric() :- 

# ---------------------------------------------

# (xi) islower() :-

# t = "hello world!!!"
# print(t.islower())

# ---------------------------------------------

# (xii) isupper() :- 

# t = "HELLO WORLD!!!"
# print(t.isupper())

# ---------------------------------------------

# (xiii) istitle() :-

# a = "HELLO HOW ARE YOU?"
# b = "Hello"
# c = "22 Names"
# d = "This is %"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# ---------------------------------------------

# (xiv) isidentifier() :-

# a = "MyFolder"
# b = "Demo222"
# c = "2Demo"
# d = "my demo"
# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

# ---------------------------------------------

# (xv) isspace() :-

# t = "   "
# print(t.isspace())

# ---------------------------------------------

# (xvi) find() :-
# syntax :- s.find(substring)
          # s.find(substring, begin, end)
# returns the index of the first occurrence of the substring in the string.

# s = "Learning Python is very easy"
# print(s.find("a"))
# print(s.find("a",3,100))

# s = "Learning Python is very esy"
# print(s.find("a",3,100)) # Here after 3 index there is no "a" though it will not give error it will give -1 output

# ---------------------------------------------

# (17) count() :-
# syntax :- s.count(substring)
          # s.count(substring,begin,end)

# s = "Devam Jha is my name"
# print(s.count("a"))
# print(s.count("a",5,35))

# ---------------------------------------------

# (18) replace() :-
# syntax :- s.replace(old string, new string)

# s = "Learning Python is very easy"
# print(s.replace("easy", "great"))
# print(s.replace("a","b",2))
# Here 2 is the count i.e. in thr above string 2 times a will be replaced by b

# ---------------------------------------------

# (19) split() :-
# syntax :- s.split(seperation)

# s = "LJ University"
# print(s.split()) # The answer of the split function will ne by default in list.
# print(len(s.split())) # To count number of words in a string

# s1 = "10-04-2024"
# print(s1.split("0"))
# print(s1.split("4")) # IMP FOR MCQ # Here a blank is genertaed

# ---------------------------------------------

# (8) Remove Punctuation using translate() function :-
# translate  with maketrans function

import string
# print(string.punctuation)
# print(len(string.punctuation))

# print(string.punctuation.replace("!", "")) # This will not remove the punctuation from the string

# print(str.maketrans("a","d","$@"))

# s = "Lea@rning Pyt$%hon is very ea$sy"
# t = s.maketrans("","",string.punctuation)
# print(  s.translate(t))

t = "Hi Sam!!!"
x = "mSa"
y = "eJo"
mytable = t.maketrans(x,y,"!") # Here ! will be removed from the String(t) and if we write string.punctuation then all the punctuations will get removed
print(t.translate(mytable))