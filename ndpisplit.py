#!/usr/bin/env python
import os
import pathlib
import shutil
import sys
import subprocess
from tqdm import tqdm


def main():
    args = sys.argv
    global path_Ndpi
    global path_Jpeg
    path_Ndpi="/mnt/ndpi/"
    path_Jpeg="/mnt/jpeg/"
    checkArgs(args)
    name = args[1]
    size = args[2]
    ndpiPath = path_Ndpi+name+"/"
    jpegPath = path_Jpeg+name+"/"
    # get directory path from ndpi
    ndpiPathList, jpegPathList = getDirectoryPath(ndpiPath,jpegPath,name)
    checkJpegDir(jpegPathList)
    split(size, ndpiPathList)
    dogTags = getDogTags(ndpiPathList, ndpiPath)
    moveJpeg(dogTags, jpegPathList)

def moveJpeg(dogTags, jpegPaths):
    pass

def getDogTags(ndpiPaths, ndpiPath):
    for item in ndpiPaths:
        item = str(item)
        item = item.replace(ndpiPath, '')
        print("dogTag: "+item)
    pass

def split(size, ndpiPaths):
    #split!!!
    print("\nsplit\n")
    processes=[]
    for ndpi in tqdm(ndpiPaths):
        processes.append(subprocess.Popen(['ndpisplit', '-m5J100', '-x40', '-z0', '-g'+size+'x'+size, ndpi]))

    print("split process check")
    for p in tqdm(processes):
        p.wait() 
    


def checkJpegDir(pathList):
    for p in pathList:
        p=pathlib.Path(p)
        if not p.exists():
            print("mkdir: "+str(p))
            os.makedirs(p)
        else:
            pass

def getDirectoryPath(ndpiPath,jpegPath,name):
    print("get directory path from ndpi")
    ndpi = pathlib.Path(ndpiPath).glob("*.ndpi")
    ndpiPaths = []
    for item in ndpi:
        ndpiPaths.append(item)
    ndpiPaths.sort()

    jpegPaths = []
    
    for item in ndpiPaths:
        length = len(str(path_Ndpi))+len(name)+1
        # print(length)
        path = jpegPath+str(item)[length:str(item).index('.ndpi')] + '/'
        jpegPaths.append(path)
    # print("jpegPaths:")
    #print(jpegPaths)
    
    jpegPaths.sort()
    for item in ndpiPaths:
        print(item)
    for item in jpegPaths:
        print(item)
    print("\n")
    return ndpiPaths, jpegPaths 


def checkArgs(args):
    if len(args) != 3:
        print("Usage: python3 ndpiPathsplit.py AR 1268")
        sys.exit(1)
    else:
        name = args[1]
        if name == "ALL":
            print("ALL madadayo sry mb :)")
            sys.exit(1)




# # split!!!
# print("split!!!")
# processes=[]
# if not name == "ALL":
#     for ndpi in tqdm(ndpiPaths):
#         i = ndpiPaths.index(ndpi)
#         dirpath = jpegPaths[i]
#         #processes.append(subprocess.Popen(['/mnt/ndpiPathsplit_rebuilded',, '-m5J100', '-x40', '-z0', '-g'+size+'x'+size, ndpi]))

# print("process check")
# for p in tqdm(processes):
#     p.wait() 


# #/mnt/ndpiPathsplit_rebuild -m5J100 -x40 -z0 -g896x896

if __name__ == "__main__":
    main()