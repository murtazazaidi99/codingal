class bike:
    def __init__(self,brand,name,color):
        self.brand=brand
        self.color=color
        self.name=name
    
    def show(self):
        print(f"this is a {self.name} {self.brand} {self.color}")

bike1=bike("RIM","BLACK","honda")
bike1.show()
    

   
 class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=Student("zaidi",17)
print(s1.name)
print(s1.marks)