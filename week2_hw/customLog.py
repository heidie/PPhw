#__future__ 가 뭐지??? 
from __future__ import print_function
#exit연산자
import re

#파일의 각 줄을 인수로 받아 에러 이름과 위치를 문자열로 돌려줌
def errorCheck(error):
	#list는 먼저 변수타임을 설정해야 한다.
	listOne = []
	listTwo = []

	#']'을 기준으로 문자열을 나누어서 리스트에 저장한다.
	listOne = error.split(']')

	#만약 위 리스트의 세번쨰 원소에 ':'이 있으면 ':'를 기준으로 문자열을 나누어서 다시 리스트에 저장한다.
	if ':' in listOne[3]:
		listTwo = listOne[3].split(':')

		#그 리스트의 0번째 원소가 에러 이름이 되고, 1번쨰 원소가 에러의 위치가 된다. 모두 문자열이다.	
		errorName = listTwo[0]
		errorLoc = listTwo[1]

	#없으면 위치가 없는 에러이므로 세번째 원소를 그대로 에러 이름으로 반환하고 위치는 없다는 문자열도 반환한다. 
	else:
		errorName = listOne[3]
		errorLoc = 'no error location'

	return errorName, errorLoc

#에러 없으면 그대로 진행, 에러나면 excep의 코드를 실행
try:
	
	#딕셔내리도 미리 변수 타이을 선언해야 한다.	
	errorDic = {}
	numErrorDic = {}

	#코드와 같은 디렉토리에 있는 'error_log'파일을 문자열(?)로 반환
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



