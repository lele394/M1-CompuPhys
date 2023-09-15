
"""

Song exo -1

"""





def eraseDoubles(song):
    
    while song.HasDoubles():
        print(song.song)
        for i in range(song.length()):

            try:
                if song.song[i] == song.song[i+1]:
                    song.song = song.song[:i] + song.song[i+2:]
                    break        

            except IndexError:
                print("indexerror yolo")
                print(song.song)
                break

    return song








class Song:
    def __init__(self, song):
        self.song = song

    def length(self):
        return len(self.song)
    
    def HasDoubles(self):
        for i in range(len(self.song) -1):
            if self.song[i] == self.song[i+1]:
                return True
        return False


#print(eraseDoubles(Song("baaabbacddc")).song)










"""

Exo 2

"""



def CreateFactorialTable():
    """Limited to <5e+8,   max fatc = 12"""

    return {
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880,
        10: 3628800,
        11: 39916800,
        12: 479001600
        }






def GetMaxFact(num):
    table = CreateFactorialTable()
    for i in [12, 11, 10, 9, 8, 7, 6, 6, 4, 3, 2, 1]:
        
        if table[i] <= num:
            return i
        


def HowMuchFit(num, fact):
    return num // CreateFactorialTable()[fact]





def GetBoxes(peas): 

    fact_dict = {}
    """fact:number"""
    while peas >0:
        maxFact = GetMaxFact(peas)
        print(peas)
        print(fact_dict)
        fits = HowMuchFit(peas, maxFact)

        peas -= CreateFactorialTable()[maxFact] * fits

        fact_dict[maxFact] = fits

    return fact_dict


print((GetBoxes(17)))

