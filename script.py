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

    

def getTemp(dir):
    for dirpath, dirnames, filenames in os.walk(dir):
        for fName in filenames:
            # print(os.path.splitext(fNames))
            if (isTempFile(os.path.splitext(fName)[1])):
                # print("Current path: ", dirpath)
                # print("Directories: ", dirnames)
                # print("Files: ", filenames)
                # print()
                fullFilePath = os.path.join(dirpath, fName)
                fileStats = os.stat(fullFilePath)
                fileSize = fileStats.st_size
                modTime = datetime.fromtimestamp(fileStats.st_mtime)
                tup = (dirpath, fName, fileSize, modTime)
                tempFiles.append(tup)
        for dName in dirnames:
            if (isTempFolder(dName)):
                fullDirPath = os.path.join(dirpath, dName)
                dirStats = os.stat(fullDirPath)
                dirSize = dirStats.st_size
                modTime = datetime.fromtimestamp(dirStats.st_mtime)
                tup = (dirpath, dName, dirSize, modTime)
                tempFolders.append(tup)
    