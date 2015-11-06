 # hw1Problem16.py
 # Created by Wilson H. Mac on 2015/10/9.

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def hwSign(x):
	if np.sign(x) == 0:
		return np.sign(-1)
	else:
		return np.sign(x)

def areNotAllCorrect(correctRecordNumPyVector, randomList):
	for i in randomList:
		if correctRecordNumPyVector[i] == 0:
			return True
	return False

def isMistakeWith(wNumPyVector,xyNumPyVector):
	if hwSign(np.sum(np.dot(wNumPyVector,xyNumPyVector[:5]))) != xyNumPyVector[5]:
		return True
	else:
		return False

def getRandomLists2000():
	randomList = np.random.random_integers(0, 399, 400 * 2000)
	return randomList.reshape(-1, 400)

inputList = []
fileName = "hw1_15_train.dat.txt"
openedFile = open(fileName, 'r')
for line in open(fileName):
	line = openedFile.readline()
	splitList = line.split()
	inputList.append(splitList)

rawInputNumPyVector = np.array(inputList, dtype = np.float)

xyNumPyVector = np.linspace(0,0,6 * len(rawInputNumPyVector))
xyNumPyVectorList = xyNumPyVector.reshape(-1,6)

for i in xrange(0, len(rawInputNumPyVector)):
	xyNumPyVectorList[i] = np.append([1], rawInputNumPyVector[i])

print 'PLA Started!'
random2000Lists = getRandomLists2000()
updateCountList = []
sum = 0.0
for iteratorFor2000 in xrange(0, len(random2000Lists)):
	correctRecordNumPyVector = np.linspace(0, 0, len(rawInputNumPyVector))
	wNumPyVector = np.linspace(0, 0, 5)
	t = 0
	lastIndex = 0
	while areNotAllCorrect(correctRecordNumPyVector, random2000Lists[iteratorFor2000]):
		for i in random2000Lists[iteratorFor2000]:
			if isMistakeWith(wNumPyVector, xyNumPyVectorList[i]):
				wNumPyVector = wNumPyVector + xyNumPyVectorList[i][:5] * xyNumPyVectorList[i][5]
				t = t + 1 
				correctRecordNumPyVector[i] = 0
				lastIndex = i
				# break
			else:
				correctRecordNumPyVector[i] = 1
	# print 'iteratorFor2000 is : ', iteratorFor2000 
	# print 'update count and last index is(zero-based) : ', t , ' ', lastIndex
	# updateCountList.append(t)
	print t
	sum += t
print 'PLA Ended!'
print 'average updating count is: ', sum/2000


