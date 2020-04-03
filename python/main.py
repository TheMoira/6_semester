# !/usr/bin/env python3.7
import math
# import cmath
# from math import sqrt
from cmath import sqrt as csqrt
from sys import argv
import copy

# print('Hello')

a = 1
b = 'f'
c = 3.4

print(f'a = {a}, type: {type(a)}')
print(f'b = {b}, type: {type(b)}')
print(f'c = {c}, type: {type(c)}')
print()
# a,*b = 2,3,4,5,'a'

# print(type(b))

print("zamiana c i d: c,d = d,c")
c,d = 1,2
print(f'NAJPIERW: c,d = {c},{d}')
c,d = d,c
print(f'TERAZ: c,d = {c},{d}')
print()

print(f'c/d ==> {c/d}')
print(f'c//d ==> {c//d}')
print()
# print(dir(math))
# # help(math.modf)

k = [1,2,'a']
print(f'k to {type(k)}, k = {k}')
k[1] = 4
print(f'k[1] = 4 ==> k = {k}')
print()

l = [[1,2,'a'],1,('c',),2,3,4]
print(f"NAJPIERW: l = {l}")
print()

l1 = l
print("l1 = l")

l1[1] = 4
print("l1[1] = 4")
print(f"TERAZ: l = {l}, l1 = {l1}")
print()
# print(id(l))
# print(id(l1))

# l1 = l[2:5]
# print(len(l1))

l2 = l[2:7:2]
# print(len(l2))
print(f"l2 = l[2:7:2] ===> l2 = {l2}")
print()

l3 = l[:]
l3[1] = 7
l3[0][1] = 8

print(f"""
l3 = l[:]
l3[1] = 7
l3[0][1] = 8

ZATEM:
l3 = {l3}
l = {l}

""")

print("REAL COPY WITH copy module:")
l4 = copy.deepcopy(l)
l4[0][1] = 7
print(f"""
!!!!!!!!!!!!!!
l4 = copy.deepcopy(l)
l4[0][1] = 7

ZATEM:
l = {l}
l4 = {l4}

""")

l5 = l[::-1]
print(f"l5 = l[::-1]  ===>  l5 = {l5}")
print()

lista = [0] * 100
lista[9] = 3
print("lista:")
print(f"lista = [0] * 100   lista[9] = 3    ===>  lista = {lista}")
print()

r1 = [[]] * 100
r1[7].append(7)

r = [[] for _ in range(100)]
r[7].append(7)

print(f"""
r1 = [[]] * 100
r1[7].append(7)

r = [[] for _ in range(100)]
r[7].append(7)

ZATEM:
r1 = {r1}
r = {r}

""")


xd = []
xd.append([4,3])
xd.extend([3,4])

print(f"""
xd = []
xd.append([4,3])
xd.extend([3,4])

ZATEM:
xd = {xd}

""")

# a = 3 if 0<d<4 else 0
# print(a)

# a = float(input('Daj mi a!' ))
# b = float(input('Daj mi b!' ))
# c = float(input('Daj mi c!' ))

# if 3<len(argv)<5:
#     a = float(argv[1])
#     b = float(argv[2])
#     c = float(argv[3])

#     eps = 1e-5


#     delta = math.pow(b,2) - 4*a*c

#     x1 = (-b + math.sqrt(delta))/(2*a) if delta > 0 else (-b + csqrt(delta))/(2*a)
#     x2 = (-b - math.sqrt(delta))/(2*a) if delta > 0 else (-b - csqrt(delta))/(2*a)

#     print(x1)
#     print(x2)

# else:
#     print('zla liczba argumentow, girl')


# k = [1,2,3,4,5,6,8,989,9,]

# for i in range(len(k)):
#     # k[i] += 1
#     if k[i] < -4:
#         break

# else:
#     print('...')

# print(k)



