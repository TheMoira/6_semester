# !/usr/bin/env python3.7
from sys import argv
from math import pow
# print(dir(""))

if len(argv) == 1:
    print('Podaj przynajmniej jeden argument')
else:
    # str1 = ''.join(argv[1:])
    print(''.join(argv[1:]))

str1 = argv[1:]
male = [i for i in str1 if i.islower()]
duze = [i for i in str1 if i.isupper()]
lb = [i for i in str1 if i.isdigit()]
nlb = [i for i in str1 if not i.isalpha()]


# print(male)
# print(duze)
# print(lb)
# print(nlb)

male_uniq = []


for i in male:
    if i not in male_uniq:
        male_uniq.append(i)


m = ' '.join(male)
# for i in male_uniq:
#     n = m.count(i)
#     male_num.append((i,n))

male_num = [(i,m.count(i)) for i in male_uniq]



male_num.sort(key = lambda x: x[1])



samogloski = ['a','o','e','i','u','y']
atab = [i for i in str1 if i.lower() in samogloski]
a1 = len(atab)
b1 = len(str1) - len(lb) - a1

fun = [(float(x),a1*float(x) + b1) for x in lb]

y = [f[1] for f in fun ]
x = [float(i) for i in lb]
sr_x = sum(x)/len(x)
sr_y = sum(y)/len(y)

print(y)


D = sum((xi-sr_x)**2 for xi in x)

a = (1/D)*sum( yi*(xi-sr_x) for xi,yi in fun)

b = sr_y - a*sr_x

print(b)

# print(f'fun = {fun}')

# print(f'male_num = {male_num}')
