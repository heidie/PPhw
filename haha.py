# export file

error  = '[Fri Oct 05 08:18:16 2012] [error] [client ::1] File does not exist: /Library/WebServer/Documents/favicon.ico'

'''
list1 =[]
list2 =[]
list3 =[]
list4 =[]
list5 =[]
listAll =[]
'''

listOne = []

if '[error]' in error:
	listOne = error.split('[error]')
	print listOne
	listOne = listOne.pop()
	print listOne
	#newString = (str)listOne[0]

	print "the type of the error is: " + listOne[13:33]
	print "the directory of the error is: " + listOne[35:]


'''
for key in listOne:
	"File does not exist")
	list1.append()

find.listAll("Invalid URI in request GET invalid")
list2.append()

find.listAll("script not found or unable to stat")
list3.append()

find.listAll("client denied by server configuration")
list4.append()

find.listAll("attemp to invoke directory as script")
list5.append()


print ("File does not exist :" + list1.len)
print ("Invalid URI in request GET invalid : " + list2.len)
print ("script not found or unable to stat :" + list3.len)
print ("client denied by server configuration :" + list4.len)
print ("attempt to invoke directory as script :" + list5.len)

print ("[Detail report]")

print("1. File does not exist")
for key in list1
	print(list1[key].find.20)


print("2. ")
'''