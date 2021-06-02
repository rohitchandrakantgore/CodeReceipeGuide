import shutil
import sys
import os

def main():
    existingDir = sys.argv[1]
    newDir = sys.argv[2]
    shutil.copytree(existingDir, newDir)

if __name__=='__main__':
    main()