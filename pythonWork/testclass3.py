class Student(object):
    @property
    def score(self):
        return self._score

    def score(self, value):
        if not instance(value, int):
            raise ValurError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self.__score = value

    def __str__(self):
        return'Student object (name: %s) %s' % (self.score, hex(id(self)))

s = Student()
s.score = 100
print(s.score)
print(s)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        print('__iter__ invoke')
        return self

    def __next__(self):
        print('__next__ invoke')
        self.a, self.b = self.b, self.a + self.b
        if self.a > 200:
            raise StopInteration()
        return self.a
    
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

print(Fib()[3])

for n in Fib():
    print(n)

