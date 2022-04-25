from Directory import Directory
from FileTreatment import File
A = Directory()
#A.excludeByFormat(exclude=False)
A.excludeByFiles(["Hola.png"])
A.excludeByFormat(".acq")
A.getFileList()

for i in A.FilesLocation:
    B= File(i)