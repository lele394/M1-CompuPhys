

def Fact(n):
    if n == 0:
        return 1
    else:
        return n*Fact(n-1)


# print(Fact(5))




def Encadre(integer, brackets):
    if brackets ==0:
        return f"{integer}"
    else:
        return f"[{Encadre(integer, brackets-1)}]"
    
# print(Encadre(23, 4))



def Reverse(inp):
    if len(inp) == 1:
        return inp
    else: 
        return Reverse(inp[1:]) + inp[0] 

# print(Reverse(input("> ")))



def sum_array(array):

    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:])



# array = [1, 2, 3, 4, 5, 6]
# result = sum_array(array)
# print("The sum of the array is:", result)






def WordGen(combi=int, letters=str, word=""):
    if combi==0:
        print("word   ", word)
        return word
    
    for i in letters:
        print(WordGen(combi-1, letters, word+i))


WordGen(2, "bi", "")






























#