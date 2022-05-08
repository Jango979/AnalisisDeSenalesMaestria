import pandas as pd
from numpy import arange


class File:
    def __init__(self, chdir, names=None, skip=0):
        if names is None:
            self.names = ["Impedance", "Phase", "Module"]
        else:
            self.names=names
        self.chdir = chdir
        self.file = self.chdir.split("\\")[-1]
        print(self.chdir.split("\\"))
        print("Leyendo archivo {}".format(self.file))

        if chdir.endswith(".csv"):
            self.formatFile = "csv"
            self.DataFrame = pd.read_csv(chdir, names=names, skiprows=skip)
        elif chdir.endswith(".xlsx"):
            self.formatFile = "excel"
            self.DataFrame = pd.read_excel(chdir, names=names, skiprows=skip)
        self.DataFrame = self.DataFrame.drop(len(self.DataFrame[:]) - 1)

    def add_time(self, no_sample=1000, to=0, tf=3):
        vTime = arange(to, tf, 1 / no_sample)
        print(vTime)
        self.DataFrame.insert(0, "Time", vTime)
        self.frec = no_sample


