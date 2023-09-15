def WordGen(combi=int, letters=str, word=""):
    if combi==0:
        print( word)
    else:
        for i in letters:
            WordGen(combi-1, letters, word+i)
        


WordGen(2, "bimp", "")