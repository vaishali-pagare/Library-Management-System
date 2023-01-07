class Book:
    def __init__(self,id,nm,auth,ctgry,cs,avlbl):
        self.id = id
        self.name = nm
        self.author = auth
        self.category = ctgry
        self.cost = cs
        self.available = avlbl

    def __str__(self):
        data = str(self.id)+","+(self.name)+","+(self.author)+","+(self.category)+","+str(self.cost)+","+str(self.available)
        return data 

