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
