import MoveFile
import os

def main():
    i = 0
    
    currentDir = MoveFile.getDir()
    dest = MoveFile.getDir()
    MoveFile.walkThrough(currentDir, dest, i)

if __name__ == "__main__":
    main()
