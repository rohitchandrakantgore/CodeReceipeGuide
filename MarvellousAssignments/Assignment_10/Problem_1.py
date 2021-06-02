import os
import sys

def main():
    dirctoryname = sys.argv[1]
    fileextensions = sys.argv[2]
    exists = os.path.isdir(dirctoryname)
    if exists:
        for foldername,subfolder,files in os.walk(dirctoryname):
            for file in files:
                if file.endswith(fileextensions):
                    print(file)
                else:
                    print('in {} directory no file with {} extension'.format(
                    dirctoryname, fileextensions
                    ))
                    break
    else:
        print('{} directory is not exists. '.format(dirctoryname))


if __name__== '__main__':
    main()


# >python Problem_1.py demos .doc
# in demos directory no file with .doc extension

# >python Problem_1.py demos .txt
# date.txt
# name.txt

# >python Problem_1.py demo .txt  
# demo directory is not exists. 