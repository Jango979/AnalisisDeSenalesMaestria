import numpy as np
import pandas as pd


class Signal2FFT():
    def __init__(self,dataframe):
        self.df = dataframe
        self.names = dataframe.names
        self.no_vector = len(self.names)



    def find_nearest(self, vector, value):
        idx = (np.abs(np.asarray(vector) - value)).argmin()
        return idx

    def smooth(self, y, box_pts):
        box = np.ones(box_pts) / box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth
    def getnames(self):
        print(self.names)
