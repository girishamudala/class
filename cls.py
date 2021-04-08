class car:
    def __init__(self,name,model,colour):
        self.name=name
        self.model=model
        self.colour=colour

    def getinfo(self):
        print("car name:{},Model:{},colour:{}".format(self.name,self.model,self.colour))

class emp:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car

    def empinfo(self):
        print("emp name:",self.ename)
        print("emp no:",self.eno)
        print("emp car info:")
        self.car.getinfo()
c=car('innova','2.5V','grey')
e=emp('durga',101,c)
e.empinfo()