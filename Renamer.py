__author__ = '206439614'

import os
import re

targetpath = "Y:\Domestic Metadata - TV and FILM\VUDU\FILM"

stringToChangeREPattern = "2015-\d\d-08"
newdate = "2015-01-08"

for root, dirs, files in os.walk(targetpath):
    for fyle in files:
        match = re.search(stringToChangeREPattern, fyle)
        if match:
            foundstring = match.group()
            print("found string: "+foundstring)
            newfylename = fyle.replace(foundstring, newdate)
            oldpath = os.path.join(root, fyle)
            newpath = os.path.join(root, newfylename)

            print("renaming "+oldpath+" to "+newpath)

            try:
                os.rename(oldpath, newpath)
            except FileExistsError:
                oldpath = os.path.join(root, fyle)
                ext = os.path.splitext(newfylename)[1]
                filename = os.path.splitext(newfylename)[0]
                index = 1
                filename = filename+"_"+str(index)+"."+ext
                newpath = os.path.join(root, filename)
                while os.path.exists(newfylename):
                    index += 1
                    newpath = os.path.join(root, newfylename+index+"."+ext)
                    print(newpath)

                os.rename(oldpath, newpath)
