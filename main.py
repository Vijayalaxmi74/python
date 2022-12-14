name="Dhanshree"
age=30
package=4.5
status=True

# primitive type of python
print("Name",name,"Type:",type(name))
print("Age:",age, "Type:",type(age))
print("Package:",package, "Type:",type(package))
print("Status:",status, "Type:",type(status))

#immutable
a=30
b=40
c=30
print("a",a,"type:",type(a),"Address:", id(a))
print("b",b,"type:",type(b),"Address:", id(b))
print("c",c,"type:",type(c),"Address:", id(c))

c=500
print("\nAfter modification")
print("a",a,"type:",type(a),"Address:", id(a))
print("b",b,"type:",type(b),"Address:", id(b))
print("c",c,"type:",type(c),"Address:", id(c))
