__author__ = 'yamakido.n'

import os
filename = os.environ.get('PYTHONSTARTUP')
print filename
if filename and os.path.isfile(filename):
    execfile(filename)
    print filename