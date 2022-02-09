#Nested Dictionary
people={
    1:{'name':'John','age':'28','sex':'Male'},
    2:{'name':'Marie','age':'33','sex':'Female'},
    3:{'name':'Tuple','age':'22','sex':'Bisex'},
        #['name','List','age','22','sex','Unknown'],
    4:{'name':'List','age':'220','sex':'Unknown'}
        #('name','Tuple','age','12','sex','Unknown')
        }
#print(people[1]['sex'])
#print(people[3][2:])
#print(type(people[3]))
#print(type(people[4]))
for x in people:
    print(people[x])
print('\n'+str(len(people)))
#following line change format dictionary 2nd line value to list
lst=list(people[2].items())
#print(type(lst))
#print dictionary 4th line to change format list
print(list(people[4].items()))
print('lst value is')
print(lst)
print(len(lst))
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "brand": "Audi",
  "model": "GTR",
  "year": 1920
}
print(thisdict)

x=1
while x<=10:
	print(x)
    x +=1

x=1
while x<=10:
    print(x)
    x +=1