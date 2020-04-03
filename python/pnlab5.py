#!/usr/bin/env python3.7
import random
import math

def gen_fibo():
    first = 0
    second = 1
    yield first
    yield second
    while True:
        first = second
        second = first + second
        yield second


gen1 = gen_fibo()

for i in gen1:
    print(i, end=' ')
    if i > 1000:
        break

def gen2_f(seq):
    for s in seq:
        if s%2:
            yield s

gen2 = gen2_f([1,2,3])

# for i in gen2:
#     print(f'{i} ')

def gen3_f(seq,max):
    for s in seq:
        yield s
        if s > max:
            break

s = 0
# fib = gen_fibo()
fib2 = gen3_f(gen1,1000)
fib_2 = gen2_f(fib2)
gen3 = gen3_f(fib_2,100)


for i in gen3:
    s += i

for i in fib2:
    print(i, end=' ')
    if i > 1000:
        break

print()

print(s)

#******************************************
#zadanie 2

def gen4_f(*ran):
    krok = 1
    min = 0
    max = ran[0]

    if len(ran) == 2:
        max = ran[1]
        min = ran[0]
    elif len(ran) == 3:
        max = ran[1]
        min = ran[0]
        krok = ran[2]

    if max < min:
        if krok < 0:  
            i = min-1   
            while i>=max:
                yield i
                i += krok

    elif krok > 0:
        i = min
        while i<max:
            yield i
            i += krok

    

gen4_1 = gen4_f(10)
gen4_2 = gen4_f(1,10)
gen4_3 = gen4_f(2,10,0.5)
gen4_4 = gen4_f(-10)
gen4_5 = gen4_f(10,1,-2)
gen4_6 = gen4_f(1,10,-2)

for i in gen4_1:
    print(i, end=' ')

print()
for i in gen4_2:
    print(i, end=' ')
    
print()
for i in gen4_3:
    print(i, end=' ')

print()
for i in gen4_4:
    print(i, end=' ')

print()
for i in gen4_5:
    print(i, end=' ')

print()
for i in gen4_6:
    print(i, end=' ')

#****************************
#zadanie 3

def row_pascal(n,prev):
    row = []
    row.append(1)

    if not n:
        return row
    
    i = 1
    while i < n:
        row.append(prev[i-1] + prev[i])
        i += 1

    row.append(1)
    return row


def pascal(n):
    i = 1
    yield [[0],[1]]
    lista = []
    lista.append([1,])


    while i <= n:
        temp = []
        temp.append(i)
        row = row_pascal(i,lista[i-1])
        temp.append(row)
        yield temp
        lista.append(row)
        i += 1
        

gen6 = pascal(9)

# for g in gen6:
#     print(g)

#**********************************
#zadanie 4

def gen7(x):
    sin = x
    k = 1

    while abs(sin - math.sin(x)) > 10**(-8):
        n = 1 + 2*k 
        sin = (((-1)**k) / math.factorial(n))*(x**n)
        i = k + 1
    yield (sin, k)

gennn = gen7(0.5 * math.pi)

# print([x for x in gennn])

#**********************************
#zadanie 5
n = 20

test = [random.randint(0,1) for _ in range(n)]
# print()
# print(test)

def gen8_f(seq):
    count = 0
    for i in seq:
        if i:
            yield count
            count = 0
        else:
            count += 1

gen8 = gen8_f(test)

suma = 0
count = 0

for g in gen8:
    count += 1
    suma += g

srednia = suma/count
print(srednia)


