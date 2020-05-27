import os
import shutil
import sys
import os.path

def main():
    i = 0
    
    #Greeting()
    welcome()
    srcFolder = getSrcDir()
    destFolder = getDestDir()
    while srcFolder == destFolder:
        print("Path for source folder and destiny folder can't be the same.")
        srcFolder = getSrcDir()
        destFolder = getDestDir()
    walkThrough(srcFolder, destFolder, i)
    end(destFolder)
    
def welcome():
    print("******************************")
    print("*     File Mover v1.0.4      *")
    print("*     Author: Zhiren Xu      *")
    print("*  published data: 5/27/20   *")
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

## Main process of file mover
# @param    srcFolderDir
#           the absolute path of source folder
# @param    destFolderDir
#           the absoulte path of destiny folder
# @param    i
#           iterator to rename file
def walkThrough(srcFolderDir, destFolderDir, i):
    #i for rename file with duplicate names
   
    for dirPath, dirNames, files in os.walk(srcFolderDir):
        hasDuplicate = 0
        display(dirPath, files)
        if len(files) == 0:
            print("Noting to move. \n")
        for fileName in files:
            if ("TOC" in fileName) or (".zip" in fileName) or (".tif" in fileName):
                srcFileDir = dirPath + "\\" + fileName
                #when copy file with same name to one directory, it will raise an error
                try:
                    moveFile(srcFileDir, destFolderDir)
                except:
                    hasDuplicate = 1
                    print("Duplicate filename detected. Change file name and move now...", end = "")
                    renameAndMove(fileName, dirPath, destFolderDir, i)
                    print("Done!")
                print(fileName, " in ", dirPath, " is moved to destination.\n")
        if hasDuplicate == 1:
            i = i + 1
        print("Target file not found. \n")

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
    print(f'Found these files in ', path, ": ")
    for file in filesList:
        print(" |-", file)
        
if __name__ == "__main__":
    main()
