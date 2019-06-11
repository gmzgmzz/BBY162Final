authorList = []

def pushAuthor(author):
    authorList.append(author)
    return True

def getAuthor(authorName):
    for author in authorList:
        if(author.name == authorName):
            return author

    return None