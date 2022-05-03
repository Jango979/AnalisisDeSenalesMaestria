from pandas import read_excel,read_csv
from numpy import arange
class File():
    def __init__(self,chdir,names=["Impedance","Phase","Module"],skip=0):
        self.chdir = chdir
        self.file= self.chdir.split("\\")[-1]
        print(self.chdir.split("\\"))
        print("Leyendo archivo {}".format(self.file))

        if chdir.endswith(".csv"):
            self.formatFile = "csv"
            self.DataFrame = read_csv(chdir, names=names, skiprows=skip)
        elif chdir.endswith(".xlsx"):
            self.formatFile ="excel"
            self.DataFrame = read_excel(chdir, names=names, skiprows=skip)
        self.DataFrame = self.DataFrame.drop(len(self.DataFrame[:]) - 1)

    def AddTime(self,noSample=1000,to=0,tf=3):
        vTime = arange(to, tf-1/noSample, 1/noSample)
        self.DataFrame.insert(0,"Time",vTime)
        self.frec = noSample


