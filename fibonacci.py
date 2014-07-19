__author__ = 'yamakido.n'

a,b = 0,1
print 'a=' + a.__str__()
print 'b=' , b.__str__()
while b <10:
    print b
    a,b=b,a+b
