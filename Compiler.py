from Directory import Directory
from FileTreatment import File
A = Directory()
#A.excludeByFormat(exclude=False)
A.excludeByFiles(["Hola.png","ChuyRelajacion.xlsx","Concentracion chuy.xlsx"])
A.excludeByFormat(".acq")
A.getFileList()


for i in A.FilesLocation:
    B= File(i)
    B.AddTime(noSample=1000,tf=180)
    print(B)