#!/usr/bin python
#-*- coding: utf-8 -*-
#
# Author: Heebum Kwak
# Email: kh-1143@hanmail.net
#

import sys

class WriteStream():
    
    def __init__(self):
        self.fp = None
        
    def open(self, filename):
        self.fp = open( filename, 'w' )
        assert( None != self.fp )
        
    def close(self):
        if self.fp:
            self.fp.close()
            self.fp = None

    def writeString(self, string):
        assert( None != self.fp )
        if self.fp:
            self.fp.write( string )
