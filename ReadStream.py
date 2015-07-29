#!/usr/bin python
#-*- coding: utf-8 -*-
#
# Author: Heebum Kwak
# Email: kh-1143@hanmail.net
#

import sys

class ReadStream():
    
    def __init__(self):
        self.fp = None
        
    def open(self, filename):
        self.fp = open( filename, 'r' )
        assert( None != self.fp )
        
    def close(self):
        if self.fp:
            self.fp.close()
            self.fp = None

    def readString(self):
        assert( None != self.fp )
        if self.fp:
            stream = self.fp.read()

        return stream
