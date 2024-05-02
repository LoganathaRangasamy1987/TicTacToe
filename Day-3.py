class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name


st1=Student()
st1.setName("Logu")
print(st1.getName())
