import os
import sys
import shutil

def main():
    existingDir = sys.argv[1]
    newDir= sys.argv[2]
    fileextension= sys.argv[3]
    exists = os.path.isdir(existingDir)
    if exists:
        for foldername,subfoldername, files in os.walk(existingDir):
            for file in files:
                if file.endswith(fileextension):
                    shutil.copy(os.path.join(foldername,file), newDir)

if __name__=="__main__":
    main()