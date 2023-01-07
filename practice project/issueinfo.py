class IssueInfo:
    def __init__(self,id,id2,nm,x):
        self.id = id
        self.userId = id2
        self.nm = nm
        self.date = x

    def __str__(self):
        data = str(self.id)+","+str(self.userId)+","+self.nm+","+str(self.date)
        return data