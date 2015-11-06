import os
import sys

import numpy as np
import matplotlib.pyplot as plt


for i in xrange(0,101):
	if i % 5 == 0:
		print i
# correctRecordNumPyVector = np.linspace(0, 0, 2000 * 400)
# correctRecordNumPyVectorList = correctRecordNumPyVector.reshape(-1, 400)
# print correctRecordNumPyVectorList

# for i in [1,4,6,9,10,222,404]:
# 	print i
# list = []
# list.append(4)
# list.append(7)
# list.append(11)
# list.append(19)
# print list
# print np.sum(list)/4
# def getRandomLists2000():
# 	randomList = np.random.random_integers(0, 399, 400 * 2000)
# 	return randomList.reshape(-1, 400)
# np.set_printoptions(threshold='nan')
# # print len(getRandomLists2000()) 
# # print getRandomLists2000()
# # np.save('randomListLog.npy', getRandomLists2000())
# a = np.load('randomListLog.npy')
# print a


# w = np.array([1,2,3,4])
# s = np.array([6,3,2,1])
# print s[3:]
# print np.sum(np.dot(w, 2)) 

# print '#####'
# print len(rawInputNumPyVector)

# print wNumPyVectorList
# print correctRecordNumPyVector
# print xyNumPyVectorList

# print '@@@@@@@@'
# print np.dot([1,2,3,4,5],xyNumPyVectorList[0][:5])
# print np.sign(-0.21112)
# correctRecordNumPyVector[199] = 0;
# print areAllCorrect(correctRecordNumPyVector)

# d[2] = d[2] + np.dot(rawInputNumPyVector[9][:4], 2)
# print d

# sum = 0
# for i in range(0,4):
# 	sum = sum + rawInputNumPyVector[9][i]

# print 'sum is : ',
# print sum

# print 'rawInputNumPyVector[9][:4] is :',
# print rawInputNumPyVector[9][:4]
# w = np.array([1,2,3,4]

# print np.dot(rawInputNumPyVector[9][:4], 2)
# print w + np.dot(rawInputNumPyVector[9][:4], 2)
# print rawInputNumPyVector.dtype



# testList = np.array([[1,2,3,4],[4,3,2,1],[0,0,0,0]])
# print testList
# testCallByReference(testList)
# print testList

# filesList = []
# tempInterfaceName = ''
# unSafeList = []

# #semaphores
# global trunkCount
# global vlanCount

# trunkCount = 0
# vlanCount = 0

# #functions
# def examineIsSafe():
# 	if trunkCount > 0 and vlanCount == 0:
# 		return False
# 	else:
# 		return True

# def getInterfaceName(interfaceLine):
# 	tempStringList = interfaceLine.split()
# 	return tempStringList[1]


# def examineSecurity(areaName):
# 	global trunkCount 
# 	global vlanCount


	# tempFile = open(areaName, 'r')

	# for line in open(areaName):
	# 	line = tempFile.readline()

	# 	if "!" in line:
	# 		if not examineIsSafe():
	# 			unSafeList.append(areaName + " " + tempInterfaceName)
	# 		trunkCount = 0
	# 		vlanCount = 0
	# 		isInterfaceLine = False

	# 	elif "interface" in line:
	# 		isInterfaceLine = True
	# 		tempInterfaceName = getInterfaceName(line)
	# 	else:
	# 		isInterfaceLine = False

	# 	if isInterfaceLine == False:
	# 		if "switchport mode trunk" in line:
	# 			trunkCount += 1
	# 		if "allowed vlan" in line:
	# 			vlanCount += 1
	# tempFile.close()






# for root, dirs, files in os.walk("./"):
# 	print root
# 	for f in files:
		
# 		if f == 'unsafeParser.py':
# 			print ' Find unsafeParser.py! '
# 		elif f == '.DS_Store':
# 			print 'Find .DS_Store! '
# 		else:
# 			examineSecurity(f)

# for unSafeInterface in unSafeList:
# 	print unSafeInterface

# print '######## End #########'



# def testCallByReference(testList):
# 	testList[2] = testList[1] -50




