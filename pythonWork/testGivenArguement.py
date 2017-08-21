def func(L=[]):
	print(hex(id(L)))
	L.append('wanli')
	return L


def func2(c=10):
	print(hex(id(c)))
	c = c + 1
	return c

def changeValue(a):
	print('id of a is', hex(id(a)))
	a = 10
	print('id of a is', hex(id(a)))
	return a

print(func())
print(func())

print('--------------------------')

print(func2())
print(func2())


print('--------------------------')
a = 100
print('id', hex(id(a)))
b = changeValue(a)
print('id of b is', hex(id(b)))
print('id of a is', hex(id(a)))
