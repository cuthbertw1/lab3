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

def isAllwoed(extention):               # WIP
    ext=["txt","png","doc","dat"]
    if extention in ext:
        return True
    else:
        return False


def getType(fileOrPath):                        # currently requires the full, absolute path to work correctly

    if os.path.isdir(fileOrPath):
        print("This is a directory")
    elif os.path.isfile(fileOrPath):
        print("This is a file")
    else:
        print("Not a file or directory")


def displayContents(directoryName):      #lists everything in a selected directory via a for loop
    if exists(directoryName):
        contents=os.listdir(directoryName)
        for content in contents:
            print(content)
    else:
        print("Error: directory not found")
def main():
    homeDirectory=os.path.expanduser("~")
    currentDirectory=os.getcwd()
    currentUser=os.getenv('USERNAME')           # change to 'USER' for linux
    print(currentDirectory)
    print(homeDirectory)
    print(currentUser)
    createDir(homeDirectory+"\CITSpring2024"+currentUser)    # change slash for linux
    print(currentDirectory)
    run=True
    files = []
    while run:

        userin=input("Enter any number of file names to create. Enter the file extention you want them all to be to finish: ")
        files.append(userin)
        if isAllwoed(userin):
            run=False

    ext=files[-1]
    files.pop()
    for file in files:
        print(file)
       # os.open(homeDirectory+"\CITSpring2024"+currentUser,4)          having issues with this on windows, need to try on vm




main()