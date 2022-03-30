from os import listdir,chdir,getcwd,path

class Local():
    def __init__(self,FolderName="Mediciones"):
        chdir(FolderName)
        self.Directory = listdir()
        print(self.Directory)
        #self.Directory=self.Directory.remove(path.basename(__file__)))
        self.name = path.basename(__file__)
        self.Directory.remove(self.name)
        print(self.Directory)
        self.Local = getcwd()
        self.FilesLocation= []
        for i in self.Directory:
            current = self.Local+"\\"+i
            print(current)

            for j in listdir(current):
                location = current+"\\"+j
                #location = location.replace("\\", "\\"*2)
                self.FilesLocation.append(location)

    def excludeByFormat(self, format = ".acq"):
        c = 0
        temp = []
        for i in self.FilesLocation:
            if i.endswith(format):
                pass
            else:
                temp.append(i)
                c=c+1
        self.FilesLocation = temp
        print(self.FilesLocation)
        print("Files removed", c)
    def excludeByFiles(self,files):
        pass
    def excludeByFolder(self,folder):
        pass
    def getFiles(self):
        print(self.FilesLocation)
A=Local()
A.excludeByFormat()