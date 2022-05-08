from Directory import Directory
from FileTreatment import File
from Signal2FFT import Signal2FFT
import pandas as pd
A = Directory()
#A.excludeByFormat(exclude=False)
A.excludeByFiles(["Hola.png", "ChuyRelajacion.xlsx", "Concentracion chuy.xlsx"])
A.excludeByFormat(".acq")
A.getFileList()

B = File(A.FilesLocation[0])
B.add_time(no_sample=1000,to=1/1000,tf=180)

#C = Signal2FFT(B)
"""
for i in A.FilesLocation:
    B= File(i)
    B.AddTime(noSample=1000,tf=180)
    print(B)
"""