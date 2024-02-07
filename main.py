#!/usr/bin/python3

import os

def exists(path):           #checks is a path exists

    if os.path.exists(path):
        return True
    else:
        return False


def renameFile(fileName, newName):

    if os.path.isfile(fileName):
        os.rename(fileName, newName)
    else:
        print("Error: file not found ")

def createDir(name):
    if not os.path.isdir(name):
        os.makedirs(name)


def getType(fileOrPath):                        # currently requires the full, absolute path to work correctly

    if os.path.isdir(fileOrPath):
        a = "Directory"
    elif os.path.isfile(fileOrPath):
        a = "File"
    else:
        a = "not a file or directory"
    return a

def displayContents(directoryName):      #lists everything in a selected directory via a for loop


    if exists(directoryName):
        print('%-25s %-25s' % ('Name', 'Type'))
        print('%-25s %-25s' % ('-----', '-----'))
        contents=os.listdir(directoryName)
        for content in contents:

            print('%-25s %-25s' % (content, getType(content)))
    else:
        print("Error: directory not found")


def createFiles(fileNamePrefix, numOfFiles, ext):
    x = 0
    y = 1
    while x < numOfFiles:
        f = open(f'{fileNamePrefix}_{y}.{ext}', 'a')
        x += 1
        y += 1
        f.close
def createSubDirectories(directoryName, numberToCreate):
    x = 0
    y = 1
    while x < numberToCreate:
        os.mkdir(directoryName+str(y))
        x += 1
        y += 1

def renameFiles(targetDirectory, currentExt, newExt):
    for files in os.listdir(targetDirectory):
        base, ext = os.path.splitext(files)
        if os.path.isfile(files):
            os.rename(files, base + "." + newExt)
    print('Renamed all accepted files')


def main():
    homeDirectory=os.path.expanduser("~")
    currentDirectory=os.getcwd()
    currentUser=os.getenv('USERNAME')           # change to 'USER' for linux
    print("Your currently directory is:", currentDirectory)
    print("Your home directory is:", homeDirectory)
    print("Your current username is:", currentUser)
    createDir(homeDirectory+"\CITSpring2024"+currentUser) # change slash for linux
    getType(homeDirectory+"\CITSpring2024"+currentUser)
    os.chdir(homeDirectory+"\CITSpring2024"+currentUser)
    newDirectory = os.getcwd()
    print("Your current directory now is", newDirectory)
    input0 = input("Name the files you want to create")
    input1 = int(input("How many files would you like to make?  "))
    while input1 <= 0:
        print("You cannot use negative numbers or zero, try again")
        input1 = int(input("How many files would you like to make?  "))
    input2 = input("What extension would you like these files to be?")
    ext = ["txt", "png", "doc", "dat"]
    while input2 not in ext:
        print("Invalid extension, please try again")
        input2 = input("What extension would you like these files to be?")
    input4 = input("Name the subfolders you want to create")
    input3 = int(input("How many subdirectories would you like to make?   "))
    while input3 < 0:
        print("You cannot use negative numbers or zero, try again")
        input3 = int(input("How many subdirectories would you like to make?   "))
    print(newDirectory)
    createFiles(input0, input1, input2)
    createSubDirectories(input4, input3)
    displayContents(newDirectory)
    input5 = input("Enter a new extension for your files")
    renameFiles(newDirectory, input2, input5)
    displayContents(newDirectory)
main()