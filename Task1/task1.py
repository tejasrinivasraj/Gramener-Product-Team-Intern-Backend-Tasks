from os import listdir
from os.path import isfile, join

def files(mypath):
    for i in listdir(mypath):
        if(isfile(join(mypath, i))):
            file.append(i)
        else:
            files(join(mypath, i));

file = []
#Enter path here
mypath = "task"

files(mypath)

print(file)
