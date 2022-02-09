'''
ac='admin'
if ac=='admin':
    print('yess')
    
admin ='Aye Co'    
print (admin[1:5])
print (admin[1:])
print (admin+' test')
if admin=="Aye Co":
    print('Admin is yes')
    print ('Admin name is ')
    print (admin*2)
    print (admin[1])
    



a = 33
b = 200
if b > a:
    print("b is greater than a")

print ("Hello")
'''

#list =['abcd',786,28,'Aye Co',82]
tinylist=[281182,'AC']
#print (list[1:3])
#print(list*2)

#print('list location is : ' + str(id(list)))
#print(id(list))
#list.insert
'''try: name= raw_input("What is ur name? ")
except NameError: pass
print ("Hi" , input("Raw input cannot use your name:"))

'''

name=input('Enter Name List with comma separate\n')
nameList=name.split(",")
print(nameList)
print(type(nameList))
print(nameList[2:])
nameTuple=tuple(nameList)
print(type(tuple(nameList)))
print (type(nameTuple))

print('convert nameTuple to list')
#convertToList=list(nameTuple)
print(type(list(nameTuple)))
'''
input_string = input("Enter Family member with comma separated")
family_list = input_string.split(",")
print("Printing all family member are")
print(type(family_list))
print(len(family_list))
print(family_list[1:])
#for name in family_list:
    #print(name)
'''
answer=""
while answer!= 'AC':
    answer = input('Try again\n')
else:
    print('your AC')