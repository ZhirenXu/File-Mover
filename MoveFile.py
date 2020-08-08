import os
import shutil
import sys
import os.path

def main():
    i = 0
    fileType = []
    welcome()
    srcFolder = getSrcDir()
    destFolder = getDestDir()
    while srcFolder == destFolder:
        print("Path for source folder and destiny folder can't be the same.")
        srcFolder = getSrcDir()
        destFolder = getDestDir()
    fileType = getFileType()
    walkThrough(srcFolder, destFolder, i, fileType)
    end(destFolder)
    
def welcome():
    print("******************************")
    print("*     File Mover v1.1.0      *")
    print("*     Author: Zhiren Xu      *")
    print("*   published data: 8/8/20   *")
    print("******************************")

def end(destFolder):
    print("The process is finished. Check your ", destFolder, " for outcome.")
    print("Press anykey to exit")
    input()
    sys.exit()
    
def getSrcDir():
    print("Please enter the source folder path: ")
    print("e.g. ", os.getcwd())
    path = input()
    print("\n")
    return path

def getDestDir():
    print("Please enter the destiny folder path: ")
    print("e.g. ", os.getcwd())
    path = input()
    print("\n")
    return path

def getFileType():
    fileSuffix = []
    fileType= ""
    
    print("Please enter suffix of files you want to move, (e.g. .zip; .txt), each at a time: ")
    fileType = input()
    fileSuffix.append(fileType)
    while (1):
        print("If you perfer to move other kind of file, please type below. \nIf not, just hit the enter key: ")
        fileType = input()
        if(len(fileType) > 0):
            fileSuffix.append(fileType)
        else:
            break
    return fileSuffix

## Main process of file mover
# @param    srcFolderDir
#           the absolute path of source folder
# @param    destFolderDir
#           the absoulte path of destiny folder
# @param    i
#           iterator to rename file
# @param    fileTypeList
#           A list contain all target files' suddix or part of file name
def walkThrough(srcFolderDir, destFolderDir, i, fileTypeList):
 for dirPath, dirNames, files in os.walk(srcFolderDir):
    display(dirPath, files)
    print("\n")
    if len(files) == 0:
        print("Noting to move. \n")
    for fileName in files:
        for suffix in fileTypeList:
            if suffix in fileName:
                srcFileDir = dirPath + "\\" + fileName
                #when copy file with same name to one directory, it will raise an error
                try:
                    moveFile(srcFileDir, destFolderDir)
                except:
                    print("Duplicate filename detected. Change file name and copy now...", end = "")
                    renameAndMove(fileName, dirPath, destFolderDir, i)
                    i = i + 1
                    print("Done!")
                print(fileName, " in ", dirPath, " is moved to destination.\n")
                
## Copy a fuile from absoulte path to a file directory
# @param    src
#           absoulte path of file which you want to copy
# @param    dest
#           absoulte pasth to a destiny folder that you are going to copy file in
def moveFile(src, dest):
    # copy2() will overwrite file with the same name, so change to read-only,
    # that will generate error get caught by try-catch,
    # in order to enter rename-copy sequence
    os.chmod(src, 0o444)
    shutil.move(src, dest)

## rename file, then copy to destiny folder, tehn change the name back.
## this is because copy2() will rewrite file if have the same file in destiny
# @param    fileName
#           the name of file that need to be copied
# @param    currentDirPath
#           the absoulte path of need-copied file
# @param    destDirPath
#           destiny folder absolute path
# @param    i
#           iterate to give copied file an unique name
def renameAndMove(fileName, currentDirPath, destDirPath, i):
    originName = ""
    
    originName = fileName
    os.chdir(currentDirPath)
    index = fileName.find('.')
    if(index == -1):
        newName = fileName + str(i)
    else:
        newName = fileName[:index] + "(" + str(i) + ")" + fileName[index:]
    os.rename(fileName, newName)
    updatedFilePath = os.path.abspath(newName)
    shutil.move(updatedFilePath, destDirPath)

## display files under this directory (no folders)
# @param    path
#           The absolute path of source folder
# @param    filesList
#           A list of files under souce folder
def display(path, filesList):
    print('Found these files in ', path, ": ")
    for file in filesList:
        print(" |-", file)
        
if __name__ == "__main__":
    main()
