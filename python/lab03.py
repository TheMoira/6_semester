#!/usr/bin/env python3.7
import random
import sys
def isPalindrom(num):
	return num == num[::-1]

dictionary = {}
while len(dictionary) < 100:
	x = random.randint(100, 10000)
	dictionary.setdefault(x, isPalindrom(str(x)))
print(dictionary)
myList = []
evenDict = {}
oddDict = {}
myList = [random.randrange(0,20) for i in range(100)]
# print(list(enumerate(myList)))
# print()
# print(myList)
for i,j in enumerate(myList):
	if j%2:
		evenDict.setdefault(j,[]).append(i)
	else:
		oddDict.setdefault(j,[]).append(i)
# print()
# print(evenDict)

newDict = {key:value if [x for x in value if not x % 3] else [value[0], value[-1]] if len(value) > 1 else [value[0]] for key, value in evenDict.items() }
# print()
# print(newDict)


if len(sys.argv) > 0:
	anotherDict = {key : random.randint(2,15) for key in range(int(sys.argv[1]))}

mySecondList = [(key, value) for key, value in anotherDict.items()]

switchedDict = {value:key for key, value in anotherDict.items()}

# print(anotherDict)
# print()
# print(mySecondList)
# print()
# print(switchedDict)

randValues = [random.randint(0,11) for _ in range(0,100)]

milionthDict = {}
for val in randValues:
	milionthDict.setdefault(val, []).append(randValues.index(val, milionthDict[val][-1] + 1 if milionthDict[val] else 0))
# print(randValues)
# print()
# print(milionthDict)

nextDict = {}
nextDict2 = {}
for key in range(10):
	nextDict.setdefault(key, random.randint(1,100))
	nextDict2.setdefault(key, random.randint(1,100))

switchedNextDict = {value:key for key, value in nextDict.items()}
switchedNextDict2 = {value:key for key, value in nextDict2.items()}

finalDict = {key:(switchedNextDict[key], switchedNextDict2[key]) for key in switchedNextDict if key in switchedNextDict2}

# print(switchedNextDict)
# print()
# print(switchedNextDict2)
# print()
# print(finalDict)