import keyword
# 33 keyword list
print(keyword.kwlist)

# multiline string declaration
names = """
hello
python!
this is multiline 
string 
declaration """

print(names)
#functions

def add(a,b):
    ans=a+b
    return ans

print("Addition : ", add(50,40))
print("Addition : ", add(50.36,40.25))
print("Addition : ", add(False,True))
print("Addition : ", add("Dhanshree", "Hood"))
print("Addition : ", add("Vijayalaxmi", "Yelchalwar"))
# print("Addition : ", add("Dhanshree",27583)) #error: can't concatenate str and int
# print("Addition : ", add("Vijayalaxmi", 27618))
print("Addition : ", add("int to str conversion: ", str(9731649854543)))

#Read dynamic inputs---input()---it reads data in a string format
"""id=int(input("Enter User ID:"))
name=input("Enter Name of user: ")
marital_status=bool(input("Enter marital status:"))
salary=float(input("Enter Salary of user:"))
print(id,"\n",name,"\n", marital_status, "\n", salary)"""

#function
def pythonJiKaTable(number):
    for i in range(1,1000):
        print(i*number)

number = int(input("Enter number: "))
pythonJiKaTable(number)

