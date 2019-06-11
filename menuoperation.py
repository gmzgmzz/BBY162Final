import commandexecutor
import fileoperation
import dynamicobjectkeeper

def getMenu():
    print("""
    1. Katalogdaki Eserleri Listele
    2. Yeni Eser Girisi
    3. Eser Adina Gore Ara
    4. Yazar Adina Gore Ara
    5. Tarihe Gore Ara
    0. Programdan Cikis Yap
    """)

    return

def executeMenuOperations(fileName):

    ans = True
    while ans:
        getMenu()

        selectedOperationId = input("Yapmak Istediginiz Islemi Giriniz: ")

        if selectedOperationId == "1":
            print("\nKatalogdaki Eserler\n")
            listWorks(fileName, True)

        elif selectedOperationId == "2":
            newWork(fileName)

        elif selectedOperationId == "3":
            searchByWorkName(fileName)

        elif selectedOperationId == "4":
            searchByAuthorName(fileName)

        elif selectedOperationId == "5":
            searchByDate(fileName)

        elif selectedOperationId == "0":
            print("\nCikis yapiliyor\n")
            ans = False

        else:
            print("Yanlis giris yaptiniz!")

    return

def listWorks(fileName, showInformation = False):

    commandexecutor.emptyAuthors()

    file = fileoperation.openFile(fileName, "r")

    lines = file.readlines()

    for line in lines:
        line = line.replace("\n", "")
        commandexecutor.fillAuthorList(line, showInformation)

    file.close()

    return

def newWork(fileName):

    listWorks(fileName)

    file = fileoperation.openFile(fileName, "a")

    commandexecutor.newWork(file)

    file.close()

    return

def searchByWorkName(fileName):

    listWorks(fileName)

    workName = input("Eser Adı: ")

    print("\nEserler: \n")

    commandexecutor.searchByWorkName(workName)

    return

def searchByAuthorName(fileName):

    listWorks(fileName)

    authorName = input("Yazar Adı: ")

    print("\nYazar ve Eserleri: \n")

    commandexecutor.searchByAuthorName(authorName)

    return

def searchByDate(fileName):

    listWorks(fileName)

    date = input("Tarih: ")

    print("\nYazar ve Eserleri: \n")

    commandexecutor.searchByDate(date)

    return