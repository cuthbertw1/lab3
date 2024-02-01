import os
def exists(path):
    if os.path.exists(path):
        return True
    else:
        return False

def renameFile(targetDirectory, currentExt, newExt):
    if isAllwoed(newExt):
        currentExt=newExt
    else:
        print("Error: please only enter allowed extentions ")


def isAllwoed(extention):
    ext=["txt","png","doc","dat"]
    if extention in ext:
        return True
    else:
        return False

def main():
    homeDirectory=os.path.expanduser("~")
    print(homeDirectory)

main()