def my_abs(x):
	if x >= 0 :
		return x
	else:
		return -x

def test(c=10):
	print('c =', c)
	c = c + 1
	return c


def nop():
	pass

def add_end(L=[]):
	print(id(L))
	L.append('END')
	return L

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum


print(my_abs(10))
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())

#print(calc([1, 5, 3, 7]))
print(calc(1, 2, 3))

print(test())
print(test())
print(test())
print(test())

print('-----------------------------------------------')

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('hello', 12, **{'hello':'world', '777':'999'})

list1 = [1,2,3,4]
if 1 in list1 :
    print('yes')
else:
    print('no')

dict1 = {'name':'changwanli', 'age':15}
if 'changwanli' in dict1:
    print('yes')
else:
    print('nono')
 
for t in dict1:
    print(dict1[t])

def person2(name, age, *, city, job):
    print(name, age, city, job)

person2('changwanli', 100, city='huainan', job='killer')
person2('changwanli', 100, **{'city':'huainan', 'job':'killer'})


def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c=0, *, d, kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f1(1, 2, 3, 'a', 'b', x=99, y=100)

f2(1, 2, 3, d='tt', kw='meng')
f2(*(1,2,3), **{'d':'lisi', 'kw':13})
f2(*[1,2,3], **{'d':'lisi', 'kw':13})
