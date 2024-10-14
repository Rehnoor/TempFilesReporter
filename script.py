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

    
def folderInteriorSize(path):
        tot = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                fullFilePath = os.path.join(dirpath, file)
                tot += os.stat(fullFilePath).st_size
        return tot


def getTemp(dir):
    # [folderName, folderSize],
    # [folderName, folderSize],
    # [folderName, folderSize]
    for dirpath, dirnames, filenames in os.walk(dir):
        for fName in filenames:
            # print(os.path.splitext(fNames))
            fullFilePath = os.path.join(dirpath, fName)
            if (not os.path.islink(fullFilePath)):
                if (isTempFile(os.path.splitext(fName)[1])):
                    fileStats = os.stat(fullFilePath)
                    fileSize = fileStats.st_size
                    modTime = datetime.fromtimestamp(fileStats.st_mtime)
                    tup = (dirpath, fName, fileSize, modTime)
                    tempFiles.append(tup)
        for dName in dirnames:
            if (isTempFolder(dName)):
                fullDirPath = os.path.join(dirpath, dName)
                dirStats = os.stat(fullDirPath)
                dirSize = dirStats.st_size + folderInteriorSize(fullDirPath)
                modTime = datetime.fromtimestamp(dirStats.st_mtime)
                tup = (dirpath, dName, dirSize, modTime)
                tempFolders.append(tup)
    

    