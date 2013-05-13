from __future__ import print_function
import re

def errorCheck(error):
	listOne = []
	listTwo = []

	listOne = error.split(']')


	if ':' in listOne[3]:
		listTwo = listOne[3].split(':')

		errorName = listTwo[0]
		errorLoc = listTwo[1]

	else:
		errorName = listOne[3]
		errorLoc = 'no error location'

	return errorName, errorLoc

try:
	
	
	errorDic = {}
	numErrorDic = {}
	reResult = ''
	
	errorFile = open('error_log')


	for line in errorFile:
		if '[error]' in line:

			errorName, errorLoc = errorCheck(line)
			#print errorName
			#print errorLoc
			
			if(not errorName in numErrorDic):
				numErrorDic[errorName] = 1
			else:
				numErrorDic[errorName] =numErrorDic[errorName] + 1
			
			if(not errorName in errorDic):
				errorDic[errorName] = []
			
			errorDic[errorName].append(errorLoc)
			
	#sReportData = errorDic
	#print (numErrorDic)
	#print (errorDic)

	with open('/Users/sohnhajeong/Documents/PP_hw/error_log2.txt', 'w') as reportFile:
		print("[log report]", file=reportFile)
	
		print ('-----The types and numbers of the errors are --------',file=reportFile)

		for errorName in numErrorDic:
			print (errorName+':', numErrorDic[errorName],"",file=reportFile)

		print ('\n')
	
		print ('-----The location of the errors are -----------------',file=reportFile)
		for errorName in errorDic:
			print (errorName+ ':',file=reportFile) 
			for errorLoc in errorDic[errorName]:
				if(not(re.search(r'($jpg|$png|$gif)', errorLoc))):	
					print (errorLoc, file = reportFile)






except IOError as detail:
		throwError(102,detail)
		print ("please check if the file is normal")



