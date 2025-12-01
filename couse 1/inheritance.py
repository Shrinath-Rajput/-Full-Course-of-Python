class parent:
    counter=10
    def __init__(self):
        print("class initilized")
    def parentfunction(self):
        print("parent fun is xcalled beinmg")
    def setcounter(self,num):
        parent.counter=num
    def showcounter(self):
        print(str(parent.counter))

class chid(parent):
    def __init__(self):
        print("class chid intilized ")
    def chidfun(self):
        print("chid well diplayed")
c=chid()
c.chidfun()
c.showcounter()
c.setcounter
c.parentfunction()


class parent1:
    def fun(self):
        print("this is a parent class ")
class chid1(parent1):
    def fun(self):
        print("ths is a choid class ")
c=chid1()
c.fun()