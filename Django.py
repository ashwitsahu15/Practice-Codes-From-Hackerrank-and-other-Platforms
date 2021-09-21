# class Employee :
#     def __init__(self,name,salary,post):
#         self.name=name 
#         self.salary=salary 
#         self.post=post
#     def printdetails(self) :
#         return self.name,self.salary,self.post

# harry=Employee()


# harry.name="HARRY"
# harry.salary=50000
# harry.post="WEB DEVELOPER"

# print(harry.printdetails())


class mycomplexnumber :
    def __init__(self,real,imag) :
        self.real=real
        self.imag=imag

    def displaycomplex(self) :
        print("{0}+{1}j".format(self.real,self.imag))
mycomplexnumber(10,20).displaycomplex()
