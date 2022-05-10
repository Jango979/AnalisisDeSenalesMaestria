from Directory import Directory
from FileTreatment import File
from Signal2FFT import Signal2FFT


def compiled():
    A = Directory("C:\\Users\\danie\\Documents\\mediciones tesis maestria\\Mediciones César\\Mediciones")
    # A.excludeByFormat(exclude=False)
    A.excludeByFiles(["Hola.png", "ChuyRelajacion.xlsx", "Concentracion chuy.xlsx"])
    A.excludeByFormat(".acq")
    A.getFileList()

    print(A.FilesLocation)
    #B = File(A.FilesLocation[0])
    #B.add_time(no_sample=1000, to=1 / 1000, tf=180)

    #C = Signal2FFT(B)
    #C.applybandpass(fLow=6, fHigh=16, order=2, lim_inf=0.1, lim_sup=15)
    #D = C.export(type="log")
    for i in A.FilesLocation:
        B = File(i)
        B.add_time(no_sample=1000,to=1/1000,tf=180)
        C = Signal2FFT(B)
        C.applybandpass(fLow=13,fHigh=21,order=2,lim_inf=12,lim_sup=22,type="log")