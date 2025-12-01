


'''class student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
s1=student("shrinath",98)
print(s1.name)'''


#function on class
'''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displaystudent(self):
        return("Studen name is "+self.name+"and age is"+str(self.age))

s=student("shrinath",18)
s.displaystudent()'''

#ATTRIBUTE
#HASSTAR

class student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
s1=student("shrinath",98)
s2=student("vk",17)
hasattr(student,"age")

setattr(student,"grade","8th")
hasattr(student,"grade")
getattr(student,"grade")
delattr(student,"grade")
hasattr(student,"grade")