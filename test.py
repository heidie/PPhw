def callRecoveryStudentNum(stubject):
	recoveryList =[]
	
	for studentName in dict_students:
	 for course in dict_student['other']['courses']:
	  if(subject == course):
	    recoveryList.append(dict_students['other']['recover']
	
	for s in recoveryList:
	  if s == '2-6':
	    num26 ++
 	  elif s == '3-8':
	    num 38 ++
	  elif s == '3-9':
	    num 39 ++
	  else s == '4-10':
	    num410 ++

	recoveryStudentNum = {}
	recoveryStudentNum['2-6'] = num26
	recoveryStudentNum['3-8'] = num38
	recoveryStudentNum['3-9'] = num39
	recoveryStudentNum['4-10'] = num410

	# 여기서 학생이 1명 이상인recovery 만 dictionary로 만들려고 했는데 dicti	#onary가 append가 안된다는 것은 알고 있지만 방법을 잘 몰라서 그냥 섰어요
	for key in recoveryStudentNum:
	  if recoverystudentNum[key] != 0
	   finalDict.append()

	print finalDict

subject = input("write the name of the subject:")

callRecoveryStudentNum(subject)
		
