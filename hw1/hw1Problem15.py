 # hw1Problem15.py
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

def areNotAllCorrect(correctRecordNumPyVector):
	for i in xrange(0, len(correctRecordNumPyVector)):
		if correctRecordNumPyVector[i] == 0:
			return True
	return False

def isMistakeWith(wNumPyVector,xyNumPyVector):
	if hwSign(np.sum(np.dot(wNumPyVector,xyNumPyVector[:5]))) != xyNumPyVector[5]:
		return True
	else:
		return False

inputList = []
fileName = "hw1_15_train.dat.txt"
openedFile = open(fileName, 'r')
for line in open(fileName):
	line = openedFile.readline()
	splitList = line.split()
	inputList.append(splitList)

rawInputNumPyVector = np.array(inputList, dtype = np.float)
correctRecordNumPyVector = np.linspace(0, 0, len(rawInputNumPyVector))

wNumPyVector = np.linspace(0, 0, 5)

xyNumPyVector = np.linspace(0,0,6 * len(rawInputNumPyVector))
xyNumPyVectorList = xyNumPyVector.reshape(-1,6)

for i in xrange(0, len(rawInputNumPyVector)):
	xyNumPyVectorList[i] = np.append([1], rawInputNumPyVector[i])

print 'PLA Started!'
wrongCount = 0
lastIndex = 0
t = 0

while areNotAllCorrect(correctRecordNumPyVector):
	for i in xrange(0, len(correctRecordNumPyVector)):
		if isMistakeWith(wNumPyVector, xyNumPyVectorList[i]):
			wNumPyVector = wNumPyVector + xyNumPyVectorList[i][:5] * xyNumPyVectorList[i][5]
			t = t + 1 
			correctRecordNumPyVector[i] = 0
			lastIndex = i
		else:
			correctRecordNumPyVector[i] = 1

print 'PLA Ended!'
print 'update count is(zero-based) : ', t
print 'last index is(zero-based) :', lastIndex


