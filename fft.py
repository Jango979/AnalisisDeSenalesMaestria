import os
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_excel
from scipy.fftpack import fft, ifft, fftfreq,fftshift
from scipy.signal import butter,sosfilt
def SenalesRapidas(Direccion,Archivo,freq=1/200):
    os.chdir(Direccion)
    File=read_excel(Archivo)
    print(File)
    TSignal=list(File["Time"])
    Imp = list(File["Imp"])
    Ph = list(File["Ph"])
    EEG = list(File["EEG"])

    plt.figure(1)
    plt.subplot(3,1,1)
    plt.plot(TSignal,Imp)
    plt.subplot(3,1,2)
    plt.plot(TSignal,Ph)
    plt.subplot(3,1,3)
    plt.plot(TSignal,EEG)

    #fft
    N=len(TSignal)
    Impf=fft(Imp)
    Phf = fft(Ph)
    EEGf = fft(EEG)

    Tf=fftshift(fftfreq(N,1/N))
    Impf = 1/(N*np.abs(Impf))
    Phf = 1/(N*np.abs(Phf))
    EEGf = 1/(N*np.abs(EEGf))

    plt.figure(2)
    plt.subplot(3,1,1)
    plt.plot(Tf,Impf)
    plt.subplot(3,1,2)
    plt.plot(Tf, Phf)
    plt.subplot(3,1,3)
    plt.plot(Tf, EEGf)

    ###BUTTER
    sos = butter(10,[4, 7],"bandpass",fs=1000,output="sos")
    filteredImpf = sosfilt(sos, Impf)
    filteredpHf = sosfilt(sos,Phf)
    filteredEEGf = sosfilt(sos, EEGf)

    LenMonoSpec = N // 2
    F = np.linspace(0, np.power(freq,-1) // 2, LenMonoSpec)

    plt.figure(3)
    plt.subplot(3,1,1)
    plt.plot(Tf,np.abs(filteredImpf))
    plt.subplot(3,1,2)
    plt.plot(Tf,np.abs(filteredpHf))
    plt.subplot(3,1,3)
    plt.plot(Tf,np.abs(filteredEEGf))

    plt.figure(4)
    plt.subplot(311)
    plt.plot(Tf[LenMonoSpec:N-1],np.abs(filteredImpf[LenMonoSpec:N-1]))
    plt.subplot(312)
    plt.plot(Tf[LenMonoSpec:N-1],np.abs(filteredpHf[LenMonoSpec:N-1]))
    plt.subplot(313)
    plt.plot(Tf[LenMonoSpec:N-1],np.abs(filteredEEGf[LenMonoSpec:N-1]))

    pri
SenalesRapidas("C:\\Users\\danie\\PycharmProjects\\pythonProject\\AnalisisDeSenalesMaestria\\Mediciones\\Dr Miguel","Concentracion2.xlsx",1/1000)
#SenalesRapidas("C:\\Users\\danie\\Documents\\mediciones tesis maestria\\Mediciones César\\Dr Miguel","Concentracion.xlsx",1/1000)
plt.show()