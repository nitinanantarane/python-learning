class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("barking")


class Cat(Mammal):
    def meaw(self):
        print("meaw")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.meaw()