






class Cell:
    def __init__(self):
        self.state = True
    
    def __repr__(self):return {True : "■", False: "□"}[self.state]




class Serie:
    def __init__(self, length):
        self.content = [Cell() for i in range(length)]





serie = Serie(10)

print(serie.content)







