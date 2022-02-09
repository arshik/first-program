students_count= 1000
rating = 4.99
is_published = False
course_name = """
Multiple  
L
i
n
e
s
"""
#print (course_name)
x=y =2
#print (x)

age = 20
#age = "pyhton" 

print ("x memory \nlocation is")
print (id(x))

print (id("Z memeory location is"))

print ("y memory location is")
print (id(y))

# take three values from user
'''name = input("Enter Employee Name: ")
salary = input("Enter salary: ")
company = input("Enter Company name: ")

# Display all values on screen
print("\n")
print("Printing Employee Details")
print("Name", "Salary", "Company")
print(name, salary, company)
print("hello" + name)'''
course = "Python"
print(len(course))
print(course[2:99])
message = "Python \'Programming\'"
print(message)
print('\nFollowing for Dictionary test')
dict={}
dict['one'] = 'This is one'
dict['two'] = 'This is two'
tinyDict={
    'name': 'John',
    'code': 2882,
    'dept' : 'sales'
}
print(dict['one'])
print(dict['two'])
print(tinyDict)
print(tinyDict.keys())
print(tinyDict.values())
print(tinyDict['code'])
print(len(dict))
tinyDict['post'] = "Officer"
print(tinyDict.keys())
print(tinyDict.items())
for x,y in tinyDict.items():
    print(y)
if "dept" in tinyDict:
    print('Yes, dept is one key in tinyDict')
    
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(':'+ p_info[key])