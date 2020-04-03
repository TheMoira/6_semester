#!/usr/bin/env python3.7
import random
from sys import argv
import random
import copy


def fun1(exp):
    size = random.randrange(0,20)
    keys = [random.random() for _ in range(size)]
    dic = {x:eval(exp.format(x)) for x in keys}
    return dic

def fun2(*lists1):
    last = []
    lists = list(lists1)

    for a in lists[0]:
        for list2 in lists[1:]:
            if a not in list2:
                break
        else:
            if a not in last:
                last.append(a)

    return last


def fun3(seq1,seq2,x=True):
    size_longer = len(seq1) if len(seq1) > len(seq2) else len(seq2)
    size_shorter = len(seq1) if len(seq1) < len(seq2) else len(seq2)
    if x:
        last = [(seq1[i],seq2[i]) for i in range(size_shorter)]
    else:
        last = [(seq1[i],seq2[i]) if i<size_shorter else (None,None) for i in range(size_longer)]
    return last

# def fun3_short(seq1,seq2,x=True):
#     len1, len2 = len(seq2), len(seq1) if (x and len(seq1) > len(seq2)) or (not x and len(seq1) < len(seq2)) else len(seq1), len(seq2)
#     last = [ (seq1[i], seq2[i]) if i<len(seq2) else (None,seq2[i]) for i in range(len(seq2)) ]

# print(fun1('x+1'))
# print(fun3([1,2,3],[2,3,4,5,6],False))
# print()
# print(fun3_short([1,2,3],[2,3,4,5,6],False))
# print(fun2([1,2,3],[2,3,4,5,6],[33,33,3,33,33],(1,2,3)))

def fun4_1(*params):
    # lista = list(params)

    max = params[0]
    for a in params:
        max = a if a > max else max
    return max

def fun4_2(fun,*params):
    return fun(*params)

def minim(*params):
    min = params[0]
    for a in params:
        min = a if a < min else min
    return min

print(fun4_1(1,2,3,4),fun4_2(fun4_1,[1,2,3,4]))

def fun5(money,coins = (10,5,2)):
    max = fun4_1(*coins[1:])
    ret = []
    i = 0
    while money >= min(*coins):
        m = money - fun4_1(*coins[i:])
        if m >= 0:
            money = m
            ret.append(coins[i])
        else:
            i = i+1

    if money > 0 :
        print("Algorytmem zachlannym nie da sie rozmienic") 

    return ret
        

def fun6(guess,start,stop,way='r'):
    count = 0
    while True:
        r = random.randint(start,stop) if way == 'r' else (stop-start)//2
        count = count + 1
        print(r)
        if r == guess:
            break
        start = start if r > guess else r
        stop = stop if r < guess else r

    return count


# print(fun5(20))
#print(fun6(18,1,20,'k'))
# print(fun2v2([1,2,3],[1,4,5,6,3],[1,3,33],(3,8,1,34)))

# print(fun1('x + 2'))