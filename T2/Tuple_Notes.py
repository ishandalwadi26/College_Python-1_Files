# TUPLE :-

# --> Exactly same as list except it is immutable
# --> Tuple is read only version of list
# --> Tuple is faster than list
# --> Data is fixed and never changes then we should go for tuple
# --> Insertion order is preserved
# --> Duplicates are allowed
# --> Heterogenous objects are allowed which means we can give multiple data types in tuple, we can even give Tuple inside Tuple
# --> we can preserve insertion order and differentiate duplcates by using index
# --> Index will play very important role in Tuple also
# --> Supports +ve and -ve indexing
# --> represent Tuple elements with () parenthesis and with comma seperator

# eg. a = 1,2,3,4,5 # This is also a Tuple
#   a = (1,2,3,4,5) This is also a Tuple
# Better is to use ()

# ----------------------------------------------------------------------------------------------------------------------------------

# t = ()
# print(type(t))
# t = (10)
# print(type(t))
# t = (10,)
# print(type(t))

# t = tuple(range(10,20,2))
# print(t)
# print(type(t))

# ----------------------------------------------------------------------------------------------------------------------------------

# (1) Accesing Elements of Tuple by using Index :-

# t = (15,25,35,45,55,65)
# print(t[0]) # 15
# print(t[-1]) # 65
# print(t[2])
# print(t[15])

# (2) Accesing Elements of Tuple by using Slicing Operator :-

# t = (15,25,35,45,55,65)
# print(t[0:3]) # (15,25,35)
# print(t[2:5])
# print(t[3:100])
# print(t[::2])
# print(t[-1:-4])
# print(t[-1:-4:-1])

# (3) Mathematical operators for Tuple :-

# + --> Concatenation
# * --> Repetition

# t1 = (15,25,35)
# t2 = (45,55,65)
# t = t1 + t2
# print(t)
# x = t1 * 3
# print(x)

# (4) Important Functions of Tuple :-

# 1. len() :- It returns the number of elements in the tuple.
# t = (15,25,35)
# print(len(t))

# 2. count() :- 
# t = (15,25,35,25,35,45,25,55,65)
# print(t.count(15))
# print(t.count(25))

# 3. index() :-
# t = (15,25,35,25,35,45,25,55,65)
# print(t.index(15))
# print(t.index(25))

# 4. sorted() :-
# By Default the answer will be in list, if we want the answer in tuple then we have to do typecasting
# t = (15,25,35,65,55,877,26)
# print(sorted(t))
# print(sorted(t,reverse=True))
# print(sorted(t,reverse=False)) # Same as sorted(t)
# print(tuple(sorted(t))) # Here we are doing typecasting to tuple

# 5. min() and max() :-
# t = (15,25,35,65,55,877,26)
# print(min(t))
# print(max(t))
# t1 = ("abc","ABC","def","dXZ")
# print(min(t1))
# print(max(t1))

# 6. reversed() :- computes reverse of a given sequence object and return it in form of list
# s = "Python"
# print(list(reversed(s)))
# print(tuple(reversed(s)))

# same can be achieved by for loop :-
# t = (15,25,35)
# for i in reversed(t):
#     print(i)

# 7. enumerate() :- 
# syntax :- enumerate(iterable, start=0)
# l1 = ("eat","sleep","repeat")
# print(list(enumerate(l1)))

# l1 = ("eat","sleep","repeat")
# print(list(enumerate(l1,12)))

# s = "devam"
# print(list(enumerate(s)))

# s1 = "Devam Swanay Hemil"

# for i in enumerate(s1):
#     print(i)

# for i,j in enumerate(s1):
#     print(i,'->',j)

# (5) Tuple Packing and Unpacking :-

# Tuple packing
# a = 15
# b = 25
# c = 35
# d = 45
# e = 55
# f = 65
# t = a,b,c,d,e,f
# print(t)

# Tuple Unpacking
# t = (15,25,35,45,55,65)
# a,b,c,d,e,f = t
# print(a,b,c,d,e,f)

# Tuple Unpacking Error
# t = (15,25,35)
# a,b = t
# print(a,b)

# (6) Loop Through Tuple :-

# Using For LOOP :-
# Directly Through Tuple
# t = ("apple","banana","cherry")
# for i in t:
#     print(i)

# Through Indexing
# for i in range(len(t)):
#     print(t[i])

# Using While LOOP :-
# t = ("apple","banana","cherry")
# i = 0

# while i<len(t): # Don't Write i<=len(t), otherwise it will give IndexError: tuple index out of range
#     print(t[i])
#     i += 1

# i = 0
# while i!=3:
#     print(t[i])
#     i += 1