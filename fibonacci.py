__author__ = 'yamakido.n'

def fib(n):
    a,b = 0,1
    print 'a=' + a.__str__()
    print 'b=' , b.__str__()
    while b <n:
        print b
        a,b=b,a+b

fib(100)