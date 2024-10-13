import os
import pathlib as Path
from datetime import datetime

tempFiles = []
tempFolders = []

testDir = os.getcwd()

def isTempFile(extName):
    return (extName == ".cache") or (extName == ".tmp") or (extName == ".log") or (extName == ".part") or (extName == ".partial")


def isTempFolder(folderName):
    return (folderName == "tmp") or (folderName == ".cache")

def stringifyBytes(bytes):
    kb = bytes/1000
    if (kb < 1):
        return str(bytes) + " Bytes"
    mb = kb/1000
    if (mb < 1):
        return str(kb) + " KB"
    gb = mb/1000
    if (gb < 1):
        return str(mb) + " MB"
    tb = gb/1000
    if (tb < 1):
        return str(gb) + " GB"
    return str(tb) + " TB"
    


for dirpath, dirnames, filenames in os.walk('/Users/sainir/repos'):
    for fName in filenames:
        # print(os.path.splitext(fNames))
        if (isTempFile(os.path.splitext(fName)[1])):
            # print("Current path: ", dirpath)
            # print("Directories: ", dirnames)
            # print("Files: ", filenames)
            # print()
            fullFilePath = os.path.join(dirpath, fName)
            fileStats = os.stat(fullFilePath)
            fileSize = stringifyBytes(fileStats.st_size)
            modTime = datetime.fromtimestamp(fileStats.st_mtime)
            tup = (dirpath, fName, fileSize, modTime)
            tempFiles.append(tup)
    for dName in dirnames:
        if (isTempFolder(dName)):
            fullDirPath = os.path.join(dirpath, dName)
            dirStats = os.stat(fullDirPath)
            dirSize = stringifyBytes(dirStats.st_size)
            modTime = datetime.fromtimestamp(dirStats.st_mtime)
            tup = (dirpath, dName, dirSize, modTime)
            tempFolders.append(tup)


print("HERE ARE THE TEMPORARY FILES AT /Users/sainir/repos")
print("----------------------------------------------------")

for tup in tempFiles:
    dirpath, fName, fileSize, modTime = tup
    print("There is a temporary file called " + fName + " at the directory " + dirpath + ".")
    print("-Size: " + fileSize + ", Last Modified: " + str(modTime))
    print()

print("HERE ARE THE TEMPORARY FOLDERS AT /Users/sainir/repos")
print("-------------------------------------------------------")
for tup in tempFolders:
    dirpath, dName, fileSize, modTime = tup
    print("There is a temporary folder called " + dName + " at the directory " + dirpath)
    print("-Size: " + fileSize + ", Last Modified: " + str(modTime))
    print()
    