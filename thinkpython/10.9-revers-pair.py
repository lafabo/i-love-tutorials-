#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

lst =[]
for i in open('words.txt').readlines():
	lst.append(i.split('\r\n')[0])


def bisection(sorted_list, word):
	min = 0
	max = len(sorted_list) - 1

	while True:
		i = (min + max) / 2

		if max < min:
			return None

		if word == sorted_list[i]:
			return i
		elif word < sorted_list[i]:
			max = i - 1
		else:
			min = i + 1


# The simplest and slowest way:
dub = []
time1 = datetime.now()
for i in lst:
	if (i not in dub) and (i[::-1] in lst):
		dub.append(i)
		dub.append(i[::-1])

		# print i, " : ", i[::-1]
print float(len(dub)/2)
print datetime.now() - time1


# Using bisect method:
dub2 = []
time2 = datetime.now()
for i in lst:
	if (i not in dub2) and (bisection(lst, i)):
		dub2.append(i)
		dub2.append(i[::-1])
print float(len(dub2)/2)
print datetime.now() - time2


# output

# i in list
# 488.0
# 0:06:58.138411

# bisect method and my algorithm
# 113411.0 <- more pares, then words in the file! awesome! todo fix this bug
# 0:06:41.011964 <- awesome economy! 17 seconds!

