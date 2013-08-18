#!/usr/bin/env python
import sys
import os
#os.environ['PYOSSIM_DIR'] = '/usr/local/ossim/python/'
try:
    ossimlib=os.environ['PYOSSIM_DIR']
    
except KeyError:
    print 'PyOSSIM python bindings not installed or PYOSSIM_DIR not set.'
    print 'Contact PlanetSasha developers'
    print 'https://github.com/epifanio/planetsasha'
    print 'Good Bye :('
    sys.exit(1)


pyossim_path = os.getenv('PYOSSIM_DIR')
pyossim_path= '/usr/local/ossim/python/lib/'
sys.path.append(pyossim_path)
print pyossim_path
from pyossim import *

def testossimncdf(argc,argv):
    print 'xx'

if __name__ == "__main__":
    init = ossimInit.instance()
    init.initialize()
    testossimncdf(len(sys.argv),sys.argv)

