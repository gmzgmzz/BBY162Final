class Author:

    workArray = []

    def __init__(self, name):
        self.workArray = []
        self.name = name

    def attachWork(self, work):
        authorWorkNames = (authorWork.name for authorWork in self.workArray)

        if work.name in authorWorkNames:
            return

        self.workArray.append(work)