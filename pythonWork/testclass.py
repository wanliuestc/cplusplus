class Student(object):
    pass


bart = Student()
print(bart)

bart.name = 'hello'
print(bart.name)


class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

one = Student2('changwanli', 123)
one.print_score()
print(one._Student2__name)
