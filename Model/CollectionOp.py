# -*- coding: utf-8 -*-
"""
Created on Thu May 14 03:14:58 2015

@author: JZA
"""


import time
import os
import library as lib
 
#Default directory path for xml data
dpath = '../../Data/'
#Do a judgement whether the defualt path exists. If not, make one
os.path.exists(dpath) or os.mkdir(dpath)
 
#Get data in XML format
lib.getXMLfile(lib.getfilename(dpath, 'data-',time.strftime('%y%m%d'),'xml'))
 
#Get data in JSON format
fo = open(lib.getfilename(dpath, 'data-',time.strftime('%y%m%d'), 'xml'), 'r')
outputname = lib.getfilename(dpath, 'data-', time.strftime('%y%m%d'), 'json')
lib.getJSONfile(fo, outputname)
 
#Get job detail data in JSON format
ifn = lib.getfilename(dpath, 'data-', time.strftime('%y%m%d'), 'json')
fo = open(ifn, 'r')
outputname = lib.getfilename(dpath, 'data-1', time.strftime('%y%m%d'), 'json')
lib.getDetailfile_1(fo, outputname)