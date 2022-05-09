from os import listdir,chdir,getcwd,path

class Directory():
    def __init__(self,FolderName="Mediciones"):
        chdir(FolderName)
        self.Directory = listdir()
        self.name = path.basename(__file__)

        self.Local = getcwd()
        self.FilesLocation= []
        for i in self.Directory:
            current = self.Local+"\\"+i

            for j in listdir(current):
                location = current+"\\"+j
                self.FilesLocation.append(location)
        print("Test 1 ✓")



    def getFileList(self):
        for file in self.FilesLocation:
            print(file)


    def excludeByFormat(self, format = ".acq", exclude=True):
        #format: type (str)
        #exclude: type (boolean) if true exclude only those who hasn't the format indicated

        c = 0
        temp = []
        #Verify optimization of if statement
        if exclude:
            for file in self.FilesLocation:
                if not file.endswith(format):
                    temp.append(file)
                    c = c + 1
        else:
            for file in self.FilesLocation:
                if file.endswith(format):
                    temp.append(file)
                    c = c + 1
        self.FilesLocation = temp
        print("Files removed {}".format(c))


    def excludeByFiles(self,files):
        c = 0
        temp = []
        for i in self.FilesLocation:
            for file in files:
                if i.endswith(file):
                    temp.append(i)
                    c=c+1
        for i in temp:
           self.FilesLocation.remove(i)
        print("Files excluded {}\nNames:{}".format(c,temp))
