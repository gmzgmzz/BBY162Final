import dynamicobjectkeeper
import work
import author
import fileoperation

def fillAuthorList(line, showInformation = False):

    splittedByDieses = line.split("#####")

    if (len(splittedByDieses) != 3):
        return

    workName = splittedByDieses[0]
    authorName = splittedByDieses[1]
    date = splittedByDieses[2]

    attachWorkToAuthor(workName, authorName, date)

    if(showInformation == True):
        print("Eser Adı: " + workName + " - Yazar Adı: " + authorName + " - Tarih: " + date)

    return

def newWork(file):

    workName = input("Eser Adi: ")
    authorName = input("Yazar Adi: ")
    date = input("Tarih: ")

    attachWorkToAuthor(workName, authorName, date)

    line = "\n" + workName + "#####" + authorName + "#####" + date

    fileoperation.writeToFile(file, line)

    return

def attachWorkToAuthor(workName, date, authorName):

    authorInstance = dynamicobjectkeeper.getAuthor(authorName)

    if authorInstance == None:
        authorInstance = author.Author(authorName)
        dynamicobjectkeeper.pushAuthor(authorInstance)

    workInstance = work.Work(workName, date)
    authorInstance.attachWork(workInstance)

    return

def searchByWorkName(workName):

    for author in dynamicobjectkeeper.authorList:
        for work in author.workArray:
            if(work.name == workName):
                print("Eser Adı: " + work.name + " - Yazar Adı: " + author.name + " - Tarih: " + work.date)

    return

def searchByAuthorName(authorName):

    for author in dynamicobjectkeeper.authorList:
        if(author.name == authorName):
            for work in author.workArray:
                print("Eser Adı: " + work.name + " - Yazar Adı: " + author.name + " - Tarih: " + work.date)

    return

def searchByDate(date):

    for author in dynamicobjectkeeper.authorList:
        for work in author.workArray:
            if(work.date == date):
                print("Eser Adı: " + work.name + " - Yazar Adı: " + author.name + " - Tarih: " + work.date)

    return

def emptyAuthors():
    dynamicobjectkeeper.authorList = []
    return

def writeToConsole(message):
    print(message)
    return