class UserInfo:
    def __init__(self,id,nm,pas,condtion):
        self.id = id
        self.name = nm
        self.pas = pas
        self.condtion = condtion

    def __str__(self):
        data = str(self.id)+","+str(self.name)+","+str(self.pas)+","+str(self.condtion)
        return data