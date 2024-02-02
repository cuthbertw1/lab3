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
def isAllwoed(extention):
    ext=["txt","png","doc","dat"]
    if extention in ext:
        return True
    else:
        return False

def getType(fileOrPath):
    if os.path.isdir(fileOrPath):
        print("This is a directory")
    elif os.path.isfile(fileOrPath):
        print("This is a file")
    else:
        print("Not a file or directory")


def displayContents(directoryName):
    if exists(directoryName):
        contents=os.listdir(directoryName)
        for content in contents:
            print(content)
    else:
        print("Error: directory not found")
def main():
    currentDirectiry=os.getcwd()
    print(currentDirectiry)
    fileCheck=input("Select file path or file")
    getType(fileCheck)
    nameCheck=input("Enter directory to out contents from: ")
    displayContents(nameCheck)
    fileName=input("enter file to rename: ")
    newName=input("Enter new file name: ")
    renameFile(fileName.strip(),newName.strip())

main()