# -*- coding: utf-8 -*-
"""
Created on Sun May 10 03:16:21 2015

@author: JZA
@collaborated work: Yuanhang Lu
"""

#Packged useful functions
###################################
import os
import urllib.request
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as BS
 
def isFileExisted(fpath, filename):
    return os.path.exists(fpath + filename)   
 
def getXMLfile(filename, turl = "http://www.careerbuilder.com/RTQ/rss20.aspx?rssid=RSS_PD&num=1000&kw="):
    if not os.path.exists(filename):
        urllib.request.urlretrieve(turl, filename)
        print("{0} is already stored".format(filename))
    else:
        print('{0} is already existed'.format(filename))
 
def getfilename(dirpath, *args):
    filename = '.'.join(args)
    return dirpath + filename
 
def getJSONfile(infilestream,outfilename):
    try:
        ntree = ET.parse(infilestream)
        root = ntree.getroot()
        fdatalist = list()
        for child in root:
            for gchild in child.findall('item'):
                cdatadic = dict()
                cdatadic['title'] = gchild.find('title').text
                cdatadic['link'] = gchild.find('link').text
                fdatalist.append(cdatadic)
        fw = open(outfilename, 'w')
        json.dump(fdatalist, fw)
        fw.close()
        print('{0} is already stored'.format(outfilename))
        return True
    except:
        print('Something wrong in stored process')
        return False
     
def getDetailfile_1(infilestream, outfilename):
    try:
        dataObj = json.load(infilestream)
        infilestream.close()
        ndataList = list()
        i = 0
        for childDict in dataObj:
            try:
                i += 1
                print(i)
                turl = urllib.request.urlopen(childDict['link'])
                soup = BS(turl)
                location = soup.find_all('span', id = 'CBBody_FloatyLocation')
                postdate = soup.find_all('span', id = 'CBBody_FloatyPosted')
                if len(location) and len(postdate):
                    souplocation = BS(str(location[0]))
                    souppostdate = BS(str(postdate[0]))
                    JobLocation = souplocation.string
                    JobPostdate = souppostdate.string
                    childDict['jobLoc'] = JobLocation
                    childDict['jobPstdt'] = JobPostdate
                    ndataList.append(childDict)
            except:
                print('Something wrong in this Link')
        fw = open(outfilename, 'w')
        json.dump(ndataList, fw)
        fw.close()
        print('{0} is already stored'.format(outfilename))
        return True
    except:
        print('Something wrong in the getDetailfile_1 process')
        return False
 
def detail(soup, ndict):
    flist = list()
    iline = soup.find_all('section', id = 'job-snapshot-section')
    if len(iline):
        isoup = BS(str(iline[0]))
        iline = isoup.find_all('strong')
        for child in iline:
            ckey = str(child)
            iisoup = BS(ckey)
            fkey = iisoup.string
            if len(fkey):
                ndict[fkey] = fvalue
        return flist
 
def merge(mlist, newlist):
    if len(mlist):
        for each in mlist:
            if type(each).__name__ == 'list':
                newlist = merge(each, newlist)
            else:
                newlist.append(each)
    return newlist