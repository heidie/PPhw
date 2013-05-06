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
	errorFile = open('error_log')


	for line in errorFile:
		if '[error]' in line:

			errorName, errorLoc = errorCheck(line)
			#print errorName
			#print errorLoc
			if (not errorName in numErrorDic):
				numErrorDic[errorName] = numErrorDic[errorName]+1

			else:
				numErrorDic[errorName]+1
			
			if(not errorName in errorDic):
				errorDic[errorName] = []

			errorDic[errorName].append(errorLoc)


	print numErrorDic
	print errorDic
	



except IOError:
		print "please check if the file is normal"

