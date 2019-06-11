import fileoperation
import commandexecutor
import menuoperation

fileName = "library.txt"

if fileoperation.isExistFile(fileName):
    menuoperation.executeMenuOperations(fileName)
else:
    commandexecutor.writeToConsole('Dosya bulunamadı! Bir library.txt dosyası oluşturup devam edebilirsiniz.')