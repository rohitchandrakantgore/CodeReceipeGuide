from genericpath import exists
import sys
import os

def main():
    directoryname = sys.argv[1]
    originalextension = sys.argv[2]
    newextension = sys.argv[3]
    exits = os.path.isdir(directoryname)
    if exits:
        for foldername,subfoldername,files in os.walk(directoryname):
            for file in files:
                f1 = os.path.join(foldername,file)
                newfile = f1.replace(originalextension, newextension)
                os.rename(f1,newfile)
    else:
        print('directory not existed')

    for folder,subfolder, file in os.walk(directoryname):
        print(file)

if __name__ == '__main__':
    main()

# >python Problem_2.py demos .txt .doc
# ['date.doc', 'name.doc']