class A(object):
    __slots__ = ('__name', '__age')
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

a = A('abc', 12)

print(a.age)
print(a.name)

print(a._A__name)
