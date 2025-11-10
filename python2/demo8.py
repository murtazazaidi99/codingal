class Student:
    def __init__(self,name,marks):
        self.name=name  #public variable
        self.__marks=marks #private variable
    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("invaild marks!")

s1=Student("ronaldo",67)
print("name",s1.name)
print("marks",s1.get_marks())
s1.set_marks(98)
print("updated marks is ",s1.get_marks())