# !/usr/bin/env python3.7
#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://www.novatel.com/assets/Web-Phase-2-2012/Solution-Pages/AttitudePlane.png)
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbulations"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

import random
from sys import argv

#zad1
def palindrome(num):
    a = str(num)
    return a[:len(a)//2] == a[len(a):len(a)//2:-1]



print(palindrome(334))

#zad2
dic = {}
i = 0

while(i<100):
    a = random.randint(100,10000)
    if a not in dic:
        i += 1
    b = dic.setdefault(a,palindrome(a))

print(dic)
print(len(dic))

#zad 3

losowe = [random.randrange(0,20) for _ in range(100)]
enu = list(enumerate(losowe))
print(enumerate(losowe))
# even = {k:0 for k in losowe if k%2 == 0}
# odd = {k:0 for k in losowe if not k%2 == 0}

even = {}
odd = {}

for i,j in enumerate(losowe):
    if i%2:
        odd.setdefault(j,[]).append(i)
    else:
        even.setdefault(j,[]).append(i)

# for k,w in odd.items(): 
#     if 0 in [j%3 for j in w]:

nowy = {k:[j for j in w if not j%3] for k,w in odd.items() if 0 in [j%3 for j in w]}

print(even)
print()
print(odd)
print()
print(nowy)

#zad4

if len(argv) > 1:
    dic2 = {i:random.randrange(2,15) for i in range(int(argv[1]))}
    lista = [(i,j) for i,j in dic2.items()]
    dic3 = {i:j for j,i in lista}
    print()
    print()
    print(dic2)
    print()
    print(lista)
    print()
    print(dic3)

#zad5

lista2 = [random.randrange(0,11) for _ in range(100)]
# dic4 = {i:[lista2.index(i,d,len(lista2)) ] for i in range(0,11)}
dic4 = {}

for i in range(0,11):
    dic4.setdefault(i,[]).append(lista2.index(i))

# print("random")
# print(lista2)
# print()
# print(dic4)

#zad6 
d1 = {k:random.randrange(1,100) for k in range(10)}
d2 = {k:random.randrange(1,100) for k in range(10)}
d1v2 = {}
d2v2 = {}

for i,j in enumerate(d1):
        d1v2.setdefault(j,i)

for i,j in enumerate(d2):  
        d2v2.setdefault(j,i)


last = {k:(d1[k],d2[k]) for k in d1 if k in d2}
print(last)
