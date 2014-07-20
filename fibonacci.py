__author__ = 'yamakido.n'

def fib(n):
    result = []
    a,b = 0,1
    print 'a=' + a.__str__()
    print 'b=' , b.__str__()
    while b <n:
        print b
        result.append(a)
        a,b=b,a+b

f100 = fib(100)
f100
