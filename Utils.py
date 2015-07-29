#!/usr/bin python
#-*- coding: utf-8 -*-
#
# Author: Heebum Kwak
# Email: kh-1143@hanmail.net
#

import sys

def makePath( parent, child ):
    parent.strip('/')
    child.strip('/')
    
    path = "{0}/{1}".format( parent, child )
    return path
