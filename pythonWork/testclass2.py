class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('dog is running...')

class Cat(Animal):
    def run(self):
        print('cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Cat))
print(isinstance(dog, Animal))


def test(animal):
    animal.run()


test(dog)
test(cat)


class A(object):
    pass

a = A()
a.score = 90;
print(a.score)

b = A()
print(b.score)
