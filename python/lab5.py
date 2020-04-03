#!/usr/bin/env python3.7
import time
from sys import version
from math import sqrt
import random
from functools import reduce

powt = 1000
N = 10000

def forStatement(n):
    lista = []
    for x in range(n):
        lista.append(x)

def listComprehension(n):
    lista = [x for x in range(n)]

def mapFunction(n):
    mapa = map(lambda x: x,range(n))

def generatorExpression(n):
    lista = (x for x in range(n))

def tester(fun):
    t1 = time.time_ns()
    for _ in range(powt):
        fun(N)
    return time.time_ns() - t1

def tester2(fun):
    t1 = time.time_ns()
    for _ in range(powt):
        lista = []
        fun(lista)
    return time.time_ns() - t1

# test=(forStatement, listComprehension, mapFunction, generatorExpression)
# for testFunction in test:
#     print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

# def dodElem(lista):
#     lista.append(2)

def sumElemFor(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma

def mapConv(lista):
    return map(lambda x: x,lista)

def genConv(lista):
    gen = (x for x in lista)
    return gen

dodElem = lambda lista: lista.append(2)
dodElem2 = lambda lista: lista.append(2**2)
sumElemSum = lambda lista: sum(lista)

test2 = (dodElem, dodElem2, sumElemFor, sumElemSum, mapConv, genConv)

for testFunction in test2:
    print(testFunction.__name__.ljust(20), '=>', tester2(testFunction))



#zad2
def calka(fun,xstart,xstop,steps):
    s = sum(map(lambda i: fun(xstart + i*((xstop-xstart)/steps)),range(steps)))
    return s

fun1 = lambda x: 2*x + 5

print(calka(fun1,0,200,200))


#zad3
def getPI():
    lista = [(random.uniform(-1,1), random.uniform(-1,1)) for _ in range(1000)]
    fits = list(filter(lambda p: p[0]**2 + p[1]**2 <= 1, lista))
    return len(fits)*4 / 1000

print(getPI())

#zad4
matrix = [[random.randint(0,30) for _ in range(5)] for i in range(10)]
matrix2 = [[random.randint(0,30) for _ in range(5)] for i in range(10)]
print(matrix)

max_in_row = list(map(lambda row: max(row),matrix))
# print(max_in_row)
max_in_col = list(map(lambda x: max(x), zip(*matrix)))
suma = list(map(lambda m: sum(m), [matrix[i].extend(matrix2[i]) for i in range(len(matrix)) ] ))
print(max_in_col)


#zad5
def fun5(xs,ys):
    n = len(xs)
    x_sr = sum(xs)/len(xs)
    D = sum((x - x_sr)**2 for x in xs)
    a = sum(ys[i]*(xs[i] - x_sr) for i in n)/D
    b = sum(y for y in ys)/n - a*sr_x
    dy = sqrt(sum(y - (a*x + b)**2)/(n - 2))
    da = dy/sqrt(D)
    db = dy*sqrt(1/n + sr_x**2/D)





