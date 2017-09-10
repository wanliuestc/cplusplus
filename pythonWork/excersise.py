def fun(s):
    i = 0
    for t in s:
        if i == 0 and t >= 'a' and t <= 'z':
            s = s[0:i] + t.upper() + s[i+1:]
        if i > 0 and t >= 'A' and t <= 'Z':
            s = s[0:i] + t.lower() + s[i+1:]
        i = i+1
    return s
    

print(fun('aBc'))

print(list(map(fun, ['aBsdfajAlskdjf', 'asdfAA'])))


from functools import reduce
def prod(l):
    def fun(x, y):
        return x*y
    return reduce(fun, l)

print(prod([1,2,3,4]))


def str2float(s):
    def fun(t):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[t]
    def fun2(m,n):
        return m*10 + n
    s = s.split('.')
    n = len(s[1])
    return reduce(fun2, list(map(fun, s[0]))) + pow(10, -n) * reduce(fun2, list(map(fun, s[1])))

print(str2float('123.23'))

print(' '.strip())
