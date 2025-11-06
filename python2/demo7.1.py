# Inheritence
 class Animals:
    def speak(self):
        print("Animal make sound")

class Dog (Animal):
    def speak (self):
        print("Dog barks")

dog=Dog()
dog.speak()
# types of Inheritence

#single Inheritence
 class Animals:
    def speak(self):
        print("Animal make sound")

class Dog (Animal):
    def speak (self):
        print("Dog barks")

dog=Dog()
dog.speak()

#multiple Inheritence
class Father:
    def quality(self):
        print("father is hard working")

class Mother:
    def nature(self):
        print("mother is care")
class child:
    def talent(self):
        print("child is talented")

c=child()
c.quality()
c.nature()
c.talent()