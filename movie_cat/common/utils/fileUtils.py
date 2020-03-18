import configparser
import os
class FileUtils():
    def readFile(path,fileName):
        pass
    def writeFile(path,fileName):
        pass
    def getConfigFilePath(fileName):
        return os.path.join(os.path.abspath(fileName),'/common/config/'+fileName)
pass