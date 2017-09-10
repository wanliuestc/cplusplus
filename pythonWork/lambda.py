f = lambda x:x*x

print(f(5))

def now():
    print('2015-2-25')

f = now
f()

print(f.__name__)
