__author__ = 'yamakido.n'

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print n ,'equals',x,'x',n/x
            break
    else:
            print n,'is a prime number'
