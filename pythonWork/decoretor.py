def log(func):
    def wrapper(*args, **kw):
        print('call begain %s():' % func.__name__)
        func(*args, **kw)
        print('call end %s():' % func.__name__)
    return wrapper


def now():
    print('2015-3-25')

now = log(now)

now()


def out(start, end):
    def decorator(func):
        def wrapper(*args, **kw):
            print(start)
            result = func(*args, **kw)
            print(end)
            return result
        return wrapper
    return decorator

def normal(a,b):
    print('normal invoke')
    return a + b

normal = out('begin', 'end')(normal)

normal(3, 4)
print(normal.__name__)
