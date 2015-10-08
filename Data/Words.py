# -*- coding: utf-8 -*-
"""
Created on Sun May 10 03:22:35 2015

@author: JZA
@collaborated work: Yuanhang Lu
"""

import xml.etree.ElementTree as ET
import re
from collections import Counter
from nltk.corpus import stopwords #python3.4 -m pip install SomePackage nltk, try nltk.download() to download stopwords data.
from stemming.porter2 import stem
import json
 
# key words extraction class
class xmlwords(list):
    self.dataObj = list()
    self.title = list()
    self.tword = list()
    self.aword = list()
    sw = stopwords.words('english')
    self.mstopwords = sw+['•', "level", "service", "rn"] # customerize s    topwords
    def __init__(self, filepath, ntop):
        self.filepath = filepath
        self.ntop = ntop
 
# import xml file
    def importf(self):
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        return root
 
# import json file
    def improtfJSON(self):
        fo = open(self.filepath)
        self.dataObj = json.load(fo)
 
# extract all titles
    def gettitle(self, root):
        for child in root:
            for job in child.findall('item'):
                jt = job.find('title').text
                self.title.append(jt)
 
# extract all titles from JSON
    def gettitlefJSON(self):
        for child in self.dataObj:
            self.title.append(child['title'])
 
# extract all key words from title
    def getkey(self):
        for string in self.title:
            self.tword+=filter(None, re.split("[ -/:,()!.]+", string.lower()))
        self.tword = [stem(word) for word in self.tword]
        self.tword = [w for w in self.tword if not w in self.mstopwords]
 
# key words frequency table
    def keytable(self, wordlist):
        return  Counter(wordlist)
 
# top ntop key words
    def keytop(self, count):
        return count.most_common(self.ntop)
 
# percentage of top ntop key words
    def toppercent(self, keytop):
        totalkey = sum([pair[1] for pair in keytop])
        topper = list()
        for i in range(self.ntop):
            topper.append((keytop[i][0], keytop[i][1]/totalkey))
        return topper
 
# add key words from job description
    def adddesc(self, root):
        mdesc = []
        for child in root:
            for job in child.findall('item'):
                desc = job.find('description').text
                mdesc.append(desc)
        wdesc = []
        for string in mdesc:
            wdesc+=filter(None, re.split("[ -/:,()!.]+", string.lower()))
        wdesc = [stem(word) for word in wdesc]
        wdesc = [w for w in wdesc if not w in self.mstopwords]
        self.aword = self.tword+wdesc