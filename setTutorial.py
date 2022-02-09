from typing import List


thisset={'melon', "Lemon", 'orange'}
print(type(thisset))
thisList=["apple",'banana','orange']
print(thisList)
print(type(thisList))
for x in thisset:
    thisList.append(x)
    #thisTuple.append(x)
    #print(x)
print(thisList)
print(type(thisList))
thisTuple=('test','final') #Tuple Array
print(type(thisTuple)) #make sure Array type is tuple or not
print(thisTuple) #check tuple array's value

#if we want to add some value in tuple array
# we change tuple to list array because tuple can't insert(read only)
#after insert some value change back again to tuple. ;)
convertList = list(thisTuple)
for y in thisset:
    convertList.append(y)
thisTuple=tuple(convertList)
print(thisTuple)
print(type(thisTuple))

a = 330
b = 330
print("A") if a == b else print("B") if a > b else print("=") 


for z in range(6):
    print(z)
    if z==0:
        next
    elif (z%2)==0:
        print('is even')
    else:
        print('is Odd')
    #z+=1
    #print(z)

people= {0:{'name':'John', 'age':'27','sex':'Male'},0.2:{'name':'Dole', 'age':'20','sex':'feMale'}}
print(people[0.2]['name'])
print(people[0]['age'])
print(people[0]['sex'])
    
num=9
flag = False
if num>1:
    for i in range(2,num):
        print('value of i is: ',i)
        if(num%i)==0:
            flag=True
            print('\nbefore break')
            break
        
if flag:
    print(num,'is not a prime number')
else:
    print(num,'is a prime')