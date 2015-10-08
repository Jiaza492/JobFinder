# -*- coding: utf-8 -*-
"""
Created on Sat May 16 03:27:05 2015

@author: JZA
"""

65
import xml.etree.ElementTree as ET # read xml file
import re # regular expression
from collections import Counter # frequency table
from nltk.corpus import stopwords # install instruction: python3.4 -m pip install SomePackage nltk, try nltk.download() to download stopwords data.
from stemming.porter2 import stem # words steming
from xmlwords import xmlwords # import our class
 
 
def main():
    # make use of xmlwords class to read 5 xmls
    xml1 = xmlwords("/Users/JZA/Workspace/JobFinder/Data/data-141115.xml", 10) # remeber to change path
    xml2 = xmlwords("/Users/JZA/Workspace/JobFinder/Data/data-141117.xml", 10)
    xml3 = xmlwords("/Users/JZA/Workspace/JobFinder/Data/data-141119.xml", 10)
    xml4 = xmlwords("/Users/JZA/Workspace/JobFinder/Data/data-141121.xml", 10)
    xml5 = xmlwords("/Users/JZA/Workspace/JobFinder/Data/data-141123.xml", 10)
    allxml = [xml1, xml2, xml3, xml4, xml5]
    inidate = 15
    mttop = []
    matop = []
 
    for ix in allxml:
        iroot = ix.importf()
        ix.gettitle(iroot)
        ix.getkey()
        itcount = ix.keytable(ix.tword)
        ittop = ix.keytop(itcount)
        ittopper = ix.toppercent(ittop)
        mttop.append(ittopper)
        print("11/{3} Top {0} key word in title: {1} percentage:{2}.".format(ix.ntop, [x for x, y in ittopper], [y for x, y in ittopper], inidate))
        ix.adddesc(iroot)
        iacount = ix.keytable(ix.aword)
        iatop = ix.keytop(iacount)
        iatopper = ix.toppercent(iatop)
        matop.append(iatopper)
        print("11/{3} Top {0} key word in job description: {1} percentage:{2}".format(ix.ntop, [x for x, y in iatopper], [y for x, y in iatopper], inidate))
        inidate = inidate + 2
    # give formatted result for ploting
    mtrankk = [ [ None for i in range(5) ] for j in range(10) ]
    mtrankp = [ [ None for i in range(5) ] for j in range(10) ]
    j = 0
 
    for dtop in mttop:
        for i in range(10):
            mtrankk[i][j] = dtop[i][0]
            mtrankp[i][j] = dtop[i][1]
        j += 1
         
    print("Title key word rank:{0}".format(mtrankk))
    print("Title key word percentage:{0}".format(mtrankp))
     
    marankk = [ [ None for i in range(5) ] for j in range(10) ]
    marankp = [ [ None for i in range(5) ] for j in range(10) ]
    j = 0
 
    for dtop in matop:
        for i in range(10):
            marankk[i][j] = dtop[i][0]
            marankp[i][j] = dtop[i][1]
        j += 1
         
    print("All key word rank:{0}".format(marankk))
    print("All key word percentage:{0}".format(marankp))
 
if __name__ == "__main__":    
    main()