import os
from pandas import read_excel
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def find_nearest(array, value):
    idx = (np.abs(np.asarray(array) - value)).argmin()
    return idx

def smooth(y, box_pts):
    box = np.ones(box_pts) / box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

Direccion ="C:\\Users\\danie\\PycharmProjects\\pythonProject\\AnalisisDeSenalesMaestria\\Mediciones\\Dr Miguel"
os.chdir(Direccion)
DF = read_excel("Concentracion2.xlsx",engine='openpyxl')


Tiempo = DF["Time"]
Impedancia = DF["Imp"]
Ph = DF["Ph"]
EEG = DF["EEG"]


TiempoMaximo = list(Tiempo)[-1]
print(TiempoMaximo)
NT = len(Tiempo)
Fs = NT/TiempoMaximo
Fn = Fs/2


ZNoOffset = signal.detrend(Impedancia,0)
pHNoOffset = signal.detrend(Ph,0)
EEGNoOffset = signal.detrend(EEG,0)


ffiltro1 = (1/TiempoMaximo) * NT


FLow = 0.1
FHigh = 8


wLow= FLow*1.25*np.pi
wHigh = FHigh*1.25*np.pi

Wn = [wLow/ffiltro1,wHigh/ffiltro1]


sos =signal.butter(2,Wn,"bandpass",output="sos")

filteredZ = signal.sosfilt(sos,ZNoOffset)
filteredpH = signal.sosfilt(sos,pHNoOffset)
filteredEEG = signal.sosfilt(sos,EEGNoOffset)

FFTZ = (np.fft.fft(filteredZ))**2
FFTpH = (np.fft.fft(filteredpH))**2
FFTEEG = (np.fft.fft(filteredEEG))**2

P2MZ = abs(FFTZ/NT) # Espectro bilateral
P1MZ = P2MZ[0:(NT//2)+1] # Espectro unilateral Z

P2MpH = abs(FFTpH/NT) # Espectro bilateral
P1MpH = P2MpH[0:(NT//2)+1] # Espectro unilateral pH

P2MEEG = abs(FFTEEG/NT) # Espectro bilateral
P1MEEG = P2MEEG[0:(NT//2)+1] # Espectro unilateral EEG

F = Fs * np.arange(0,len(P2MZ))/len(P2MZ)
fM = Fs * np.arange(0,len(P1MZ))/len(P1MZ)

limInf = find_nearest(fM,0.5)
limSup = find_nearest(fM,31)

plt.figure(1)
plt.subplot(311)
plt.plot(Tiempo,Impedancia)
plt.subplot(312)
plt.plot(Tiempo,Ph)
plt.subplot(313)
plt.plot(Tiempo,EEG)

plt.figure(2)
plt.subplot(311)
plt.plot(Tiempo,ZNoOffset)
plt.subplot(312)
plt.plot(Tiempo,pHNoOffset)
plt.subplot(313)
plt.plot(Tiempo,EEGNoOffset)

plt.figure(3)
plt.subplot(311)
plt.plot(F,P2MZ)
plt.subplot(312)
plt.plot(F,P2MpH)
plt.subplot(313)
plt.plot(F,P2MEEG)

plt.figure(4)
plt.subplot(311)
plt.plot(fM,P1MZ)
plt.subplot(312)
plt.plot(fM,P1MpH)
plt.subplot(313)
plt.plot(fM,P1MEEG)

plt.figure(5)
plt.subplot(311)
plt.plot(fM[limInf:limSup],P1MZ[limInf:limSup])
plt.subplot(312)
plt.plot(fM[limInf:limSup],P1MpH[limInf:limSup])
plt.subplot(313)
plt.plot(fM[limInf:limSup],P1MEEG[limInf:limSup])

limInf = find_nearest(fM,0.1)
limSup = find_nearest(fM,7)
#####Normaliza
P1MZ=P1MZ/np.max(P1MZ)
P1MEEG=P1MEEG/np.max(P1MEEG)
P1MpH=P1MpH/np.max(P1MpH)

plt.figure(6)

plt.plot(fM[limInf:limSup],smooth(P1MZ[limInf:limSup],box_pts=5),label="Impendance")
plt.plot(fM[limInf:limSup],smooth(P1MpH[limInf:limSup],box_pts=5),label="Phase")
plt.plot(fM[limInf:limSup],smooth(P1MEEG[limInf:limSup],box_pts=5),label="EEG")
plt.legend()
plt.show()