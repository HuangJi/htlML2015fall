 # hw1Problem20.py
 # Created by Wilson H. Mac on 2015/10/10.

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
	randomList = np.random.random_integers(0, 499, 500 * 2000)
	return randomList.reshape(-1, 500)

def getRandomChooseWrongPointWith(correctRecordNumPyVector):
	while 1:
		index = np.random.random_integers(0, 499)
		if correctRecordNumPyVector[index] == WrongFlag:
			return index

def getErrorRate(wNumPyVector, xyTestNumPyVectorList, randomList):
	points = 500.00
	for i in randomList:
		if isMistakeWith(wNumPyVector,xyTestNumPyVectorList[i]):
			points -= 1
	return (500.0 - points) / 5 


inputList = []
fileName = "hw1_18_train.dat.txt"
openedFile = open(fileName, 'r')
for line in open(fileName):
	line = openedFile.readline()
	splitList = line.split()
	inputList.append(splitList)

rawInputNumPyVector = np.array(inputList, dtype = np.float)

inputList = []
testFileName = "hw1_18_test.dat.txt"
openedFile = open(testFileName, 'r')
for line in open(testFileName):
	line = openedFile.readline()
	splitList = line.split()
	inputList.append(splitList)

rawInputTestNumPyVector = np.array(inputList, dtype = np.float)


xyNumPyVector = np.linspace(0,0,6 * len(rawInputNumPyVector))
xyNumPyVectorList = xyNumPyVector.reshape(-1,6)
xyTestNumPyVector = np.linspace(0,0,6 * len(rawInputTestNumPyVector))
xyTestNumPyVectorList = xyTestNumPyVector.reshape(-1,6)

for i in xrange(0, len(rawInputNumPyVector)):
	xyNumPyVectorList[i] = np.append([1], rawInputNumPyVector[i])
	xyTestNumPyVectorList[i] = np.append([1], rawInputTestNumPyVector[i])

print 'PLA Started!'

random2000Lists = getRandomLists2000()
updateCountList = []
sum = 0.0
WrongFlag = 9
CorrectFlag = 1
for iteratorFor2000 in xrange(0, len(random2000Lists)):
	correctRecordNumPyVector = np.linspace(0, 0, 128 * len(rawInputNumPyVector))
	correctRecordNumPyVectorList = correctRecordNumPyVector.reshape(-1, 500)
	wNumPyVector = np.linspace(0, 0, 128 * len(rawInputNumPyVector))
	wNumPyVectorList = wNumPyVector.reshape(-1, 5)
	wCorrectList = np.linspace(0, 0, len(rawInputNumPyVector))
	t = 0
	lastIndex = 0
	pocketTofW = 0
	wCorrectCounter = 0
	while t < 100:
		for i in random2000Lists[iteratorFor2000]:
			if isMistakeWith(wNumPyVectorList[t], xyNumPyVectorList[i]):
				correctRecordNumPyVectorList[t][i] = WrongFlag
			else:
				correctRecordNumPyVectorList[t][i] = CorrectFlag
				wCorrectList[t] += 1
				if wCorrectList[pocketTofW] < wCorrectList[t]:
					pocketTofW = t

		wrongPoint = getRandomChooseWrongPointWith(correctRecordNumPyVectorList[t])
		wNumPyVectorList[t+1] = wNumPyVectorList[t] + xyNumPyVectorList[wrongPoint][:5] * xyNumPyVectorList[wrongPoint][5]
		t += 1
	errorRate = getErrorRate(wNumPyVectorList[99], xyTestNumPyVectorList, random2000Lists[iteratorFor2000])
	# print 'iteratorFor2000 is : ', iteratorFor2000 
	# print 'pocket t is: ', pocketTofW
	# print 'pocket w vector is:', wNumPyVectorList[pocketTofW]
	print errorRate
	sum += errorRate
print 'PLA Ended!'
print 'Average error rate is: ', sum/2000


