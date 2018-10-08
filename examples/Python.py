#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from sys import io

class Foo():
    def __init__(self, name = "World!"):
        self.name = name
        self.is_test = True

if __name__ == "__main__":
    instance = Foo()
    print "Hello, %s" % instance.name
    # Comments
    for i in range( 1, 100):
      a = [ x+1 for x in range(1, i) ]
    
#	 print "Mixing tabs and spaces is bad"
