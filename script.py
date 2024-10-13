import os

tempFiles = []
tempFolders = []



def isTempFile(extName):
    return (extName == ".cache") or (extName == ".tmp") or (extName == ".log") or (extName == ".part") or (extName == ".partial")


def isTempFolder(folderName):
    return (folderName == "tmp") or (folderName == ".cache")


for dirpath, dirnames, filenames in os.walk('/Users/sainir/repos'):
    for fName in filenames:
        # print(os.path.splitext(fNames))
        if (isTempFile(os.path.splitext(fName)[1])):
            # print("Current path: ", dirpath)
            # print("Directories: ", dirnames)
            # print("Files: ", filenames)
            # print()
            tup = (dirpath, fName)
            tempFiles.append(tup)
    for dName in dirnames:
        if (isTempFolder(dName)):
            tup = (dirpath, dName)
            tempFolders.append(tup)


print("HERE AT THE TEMPORARY FILES AT /Users/sainir/repos")
print("----------------------------------------------------")

for tup in tempFiles:
    dirpath, fName = tup
    print("There is a temporary file called " + fName + " at the directory " + dirpath)
    print()

print("HERE ARE THE TEMPORARY FOLDERS AT /Users/sainir/repos")
print("-------------------------------------------------------")
for tup in tempFolders:
    dirpath, dName = tup
    print("There is a temporary folder called " + dName + " at the directory " + dirpath)
    print()
    