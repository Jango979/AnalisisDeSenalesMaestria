import pandas as pd

class File():
    def __init__(self,chdir):
        self.chdir = chdir
        self.File= self.chdir.split("\\")[-1]
        print(self.File)
        """
        if chdir.endswith(".csv"):
            self.File=
        elif chdir.endswith(".xlsx"):
            pass
        """
    def AddTime(self,NoSample=1000,T=3):
        pass
