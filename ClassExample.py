class Book:
    #Instance methid as self is the default argument
    #Self is a default argument and value for it is implicitly provided by pvm
    #constructor method
    def __init__(self): #we write constructor like __init__
        print("Default constructor")


    def __init__(self,bookname,authorname,price): #local variables
        self.bookname = bookname
        self.authorname = authorname
        self.price = price

    def show(self):
        print(self.bookname,"\n",self.authorname,"\n",self.price)

obj1=Book("Twilight", "asduwahydkui", 2000) #Object
obj1.show()

# it will not take default constructor bcoz it is considering the latest method i.e. show() method right now, which is implemented at last
# obj2 = Book()
# obj2.show()

# if we write obj2 before obj1, then it will consider the obj2 n give error for obj1