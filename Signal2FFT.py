import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt

class Signal2FFT():
    def __init__(self,dataframe):
        self.DF = dataframe
        self.names = dataframe.names
        self.no_vector = len(self.names)
        self.analogsInputsNames = list(self.DF.DataFrame.columns.values)


        if not hasattr(self.DF.DataFrame,"Time"):
            raise RuntimeError("Vector tiempo no encontrado")
        else:
            print("Vector tiempo localizado\nTest 4 ✓")
            self.VectorTime = np.around(list(self.DF.DataFrame.Time),decimals=3)
            #print(self.analogsInputsNames)

        self.TimeMax = list(self.VectorTime)[-1]
        self.NT = len(self.VectorTime)
        self.Fs = self.NT / self.TimeMax
        self.Fn = self.Fs / 2
        self.ff1= (1/self.TimeMax) * self.NT

        print("Test 5 ✓ ")


    def applybandpass(self, fLow=1, fHigh=31, order=2, lim_inf=0.1, lim_sup=31,type=type):
        self.bandpassjoin(fLow=fLow,fHigh=fHigh,order=order)
        self.plotfft(lim_inf=lim_inf,lim_sup=lim_sup,type=type)
        print("Test 7 ✓\nThe End")



    def bandpassjoin(self,fLow=1, fHigh=31, order=2):
        self.VSignals={}
        self.analogsInputsNames.pop(0)
        #rint(self.analogsInputsNames)
        for i,j in zip(self.analogsInputsNames, self.names):
            #print(self.analogsInputsNames)
            SignalOffset = self.detrendSignal(self.DF.DataFrame[i])
            filtered = signal.sosfilt(self.bandpass(fLow=fLow,fHigh=fHigh,order=order),SignalOffset)
            ffiltered = np.fft.fft(filtered)**2
            P2M = abs(ffiltered/ self.NT)  # Espectro bilateral
            P1M = P2M[0:(self.NT // 2) + 1]
            P1M = P1M/np.max(P1M)
            self.VSignals.update({j : P1M})
            self.fM = self.Fs * np.arange(0,len(P1M))/len(P1M) ####ver como reducir a 1 sentencia por P1M
        print("Test 6 ✓")


    def bandpass(self,fLow=1,fHigh=31,order=6):
        wLow = fLow*1.25*np.pi
        wHigh = fHigh*1.25*np.pi
        Wn = [wLow/self.ff1, wHigh/self.ff1]
        return signal.butter(order, Wn, "bandpass", output="sos")

    def detrendSignal(self,sgn,offset=0):
        return signal.detrend(sgn,offset)


    def find_nearest(self, vector, value):
        idx = (np.abs(np.asarray(vector) - value)).argmin()
        return idx

    def smooth(self, y, box_pts):
        box = np.ones(box_pts) / box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth

    def getnames(self):
        print(self.names)

    def plotfft(self, type=None, lim_inf=0.1, lim_sup=31,smooth_box_pts=11):

        lim_inf = self.find_nearest(self.fM,lim_inf)
        lim_sup = self.find_nearest(self.fM,lim_sup)
        if type is None:
            """Type: linear / log"""
            type = "linear"

        if type == "linear":
            for i in self.VSignals.keys():
                plt.plot(self.fM[lim_inf:lim_sup],
                         signal.medfilt(self.smooth(self.VSignals[i][lim_inf:lim_sup],box_pts=smooth_box_pts)),
                         label=i)
            plt.legend()
            plt.show()
        elif type == "log":
            for i in self.VSignals.keys():
                plt.plot(self.fM[lim_inf:lim_sup],
                         signal.medfilt(self.smooth(self.VSignals[i][lim_inf:lim_sup],box_pts=smooth_box_pts)),
                         label=i)
            plt.yscale("log")
            plt.legend()
            plt.title(self.DF.file)
            plt.show()


    def export(self,name="Concentracionfftdata.csv",type = None,lim_inf=0.1,lim_sup=10):
        output = {}
        lim_inf = self.find_nearest(self.fM, lim_inf)
        lim_sup = self.find_nearest(self.fM, lim_sup)
        ftimeout = np.around(self.fM[lim_inf:lim_sup],4)
        output.update({"freq":ftimeout})
        for i in self.VSignals.keys():
            output.update({i:pow(10, self.VSignals[i][lim_inf:lim_sup])})
        output = pd.DataFrame(output)
        output.to_csv(name)
        return output







