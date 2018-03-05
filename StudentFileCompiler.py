# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:07:27 2018

@author: Sempiternus
"""

from os import listdir
from os.path import isfile, join
import pandas as pd

#Make list of all the files in target folder
folderList = [f for f in listdir("D:\FILES\School\McKell LAB\quizzes") if isfile(join("D:\FILES\School\McKell LAB\quizzes", f))]
folderList

#Makes an empty list for the path names of the files in the target folder
filePathlist = []

#Creates a list of the full paths for each file in the folder
for f in folderList:
    filePathlist.append("D:\FILES\School\McKell LAB\quizzes\\" + f)

#Opens up linker file and columns
linkerFile = pd.read_csv("D:\FILES\School\McKell LAB\LinkerFile.csv")

#Checks if names from linkerFile are in current file
for f in filePathlist:
    fileOpen = pd.read_csv(f)
    for row in fileOpen:
        if ((fileOpen['LastName'] == linkerFile.lastname) & (fileOpen['FirstName'] == linkerFile.firstname)).any() is True:
            print('yes')
        else:
            counter.append(1)

counter






for row in linkerFile:
    if linkerFile['lastname']

for f in filePathlist:
    fileOpen = pd.read_csv(f)
    for row in fileOpen:
        for row in linkerFile:
            if linkerFile.lastname and linkerFile.firstname in row:
                print ('yes')
            else:
                print ('no')
        
    
    
    


#Creates a list of each column on the linker file
lastnameList = linkerFile['lastname']
firstnameList = linkerFile['firstname']
semesterList = linkerFile['semester']
sidList = linkerFile['sid']


#Opens up each file in the folder and edits the columns
for f in filePathlist:
    fileOpen = pd.read_csv(f)
    for row in fileOpen:
        for f in lastnameList:
            if f in row
                


    