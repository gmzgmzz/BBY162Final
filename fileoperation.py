import os
import commandexecutor

def isExistFile(fileName):
    
    if os.path.exists(fileName):
        return True

    return False

def openFile(fileName, mode):
    try:
        currentFile = open(fileName, mode)
        return currentFile
    except:
        commandexecutor.writeToConsoleAndFile("Dosya açılırken hata oluştu!")
        return None

def writeToFile(file, line):

    if(file == None):
        print("Dosya Bulunamadı!")
        return

    file.write(line)

    return

def closeFile(file):
    file.close()
    return