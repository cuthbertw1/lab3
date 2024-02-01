import os
class file:
    def __init__(self, path):
        self.path=path


    def exists(self):
        if os.path.exists(self.path):
            return True
        else:
            return False



