'''first = "Mosh"
Last = "Hamedani"
full  = f"{first}{Last }"
print(full)

x= 10
print(x)
print(bin(x))
print(hex(x))

x=0b10
print((x))
print(hex(x)+"\n")
print(bin(x)+"\n")

x=0x12c
print(x)
print(hex(x))
print(bin(x))

'''
people={
    1:{'name':'John','age':'28','sex':'Male'},
    2:{'name':'Marie','age':'33','sex':'Female'},
    3:{'name':'Tuple','age':'22','sex':'Bisex'}
}
people1={'name':'people1','age':'22','sex':'Bisex'}
print('people dictionaries are')
print(people)
thisList=['apple','banana','orange']
print('thisList list values are')
print(thisList)
#thisList.extend(people[2].items())
#thisList.extend(people1.items())
print(len(thisList))
#print(thisList)

#following codes are retrive values only from people1 dictionary
for z in people1:
    thisList.append(people1.get(z))
    #extend method add one aplphabet as one item 
    # ad as : "p,e,o,p,l,e,1,....,e,x"
    #thisList.extend(people1.get(z))
    #print (people1.get(z))
print(thisList)
print(len(thisList))
#print(type(people))
#following codes are another way to retive values only
#from people1 dictionary
for a,b in people1.items():
    #print("b value is ")
    #print(b)
    thisList.append(b)
print(thisList)
print(len(thisList))

#following code  retrive value only from Nested dictionary "people"
for p_id,p_info in people.items():
    #print("\nPerson ID:", p_id)
   # print(p_info)
    
    for key in p_info:
        #print (key)
        #print(':',p_info[key])
        thisList.append(p_info[key])
print(thisList)
print(len(thisList))

