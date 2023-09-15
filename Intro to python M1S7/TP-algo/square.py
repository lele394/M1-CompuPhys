"""

Exo 1

"""
import math



def CreateMatrix(size=(10,10), proba_fill=0.2):

    matrix = [["1" for i in range(size[1])]]

    for i in range(size[0]-2):
        matrix.append(CreateLine(size[1], proba_fill))

    matrix.append(["1" for i in range(size[1])])

    return (size, matrix)

    
    


from random import random as rd
def CreateLine(size, proba_fill):
    line = ["0" for i in range(size)] 
    for index in range(len(line)):
        if rd() < proba_fill:
            line[index] = "1"
        else: 
            line[index] = "0"
    
    line[0] = "1"
    line[-1] = "1"
    return line











def MakeItAList(input):
    lines = input.split("\n")

    l0 = lines[0].split(" ")
    size = (int(l0[0]), int(l0[1])) #==================

    lines.pop(0)

    matrix = [i.split(" ") for i in lines]

    return(size, matrix)




def GetAllSolid(input):
    matrix = input[1]

    size = input[0]

    solid = []

    #solid inside matrix
    x = 0
    for line in matrix:
        y = 0
        for cell in line:
            if cell == "1":
                solid.append((x, y))
            y+=1
        x+=1




    """
    ! no way that works yolo

    #edge conditions
    for i in range(size[0]):
        solid.append((-1, i))

    for i in range(size[0]):
        solid.append((size[1], i))

    for i in range(size[1]):
        solid.append((i, -1))

    for i in range(size[1]):
        solid.append((i, size[0]))
    """
    return solid
            





def GetDistances(input, solid):
    matrix = input[1]
    
    min_dists = []

    #for each cell :
    for line in range(len(matrix)):
        for index in range(len(matrix[line])):
            #check if is empty
            if matrix[line][index] == "0":
                #max distance possible for sure
                dist = input[0][0] * input[0][1]

                #foreach solid get distance and check if max
                for cell in solid:
                    new_dist = math.sqrt( (cell[0]-line)**2 + (cell[1]-index)**2   )

                    if new_dist<dist:
                        dist = new_dist

                #append found min dist
                min_dists.append((dist , (line, index)))


    return min_dists



def DebugGrid(info, input):

    size = input[0]

    grid = [[ "□" for i in range(size[1] )] for i in range(size[0] )]


    for i in info:
        grid[i[0]][i[1]] = "■"

    print("   ", "".join([str(i%10 )for i in range(size[1])]))
    c=0
    for line in grid:
        print(str(c%10), " ", "".join(line))
        c+=1







def main():
    input ="""6 7
1 0 0 1 0 0 1
0 0 0 0 0 0 0
1 0 0 0 0 0 0
0 0 0 0 0 0 0
0 1 0 0 0 0 1
1 0 0 0 1 0 1 """

    input ="""8 9
1 1 1 1 1 1 1 1 1
1 1 0 0 1 0 0 1 1
1 0 0 0 0 0 0 0 1
1 1 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 1
1 0 1 0 0 0 0 1 1
1 1 0 0 0 1 0 1 1 """


    input2="""5 7
0 0 0 1 1 1 1
0 0 0 1 1 1 1
0 0 0 1 1 1 1
1 1 1 1 1 0 0
1 1 1 1 1 0 0 """


    input3="""7 9
1 1 1 1 1 1 1 1 1
1 0 0 0 1 1 1 1 1
1 0 0 0 1 1 1 1 1
1 0 0 0 1 1 1 1 1
1 1 1 1 1 1 0 0 1
1 1 1 1 1 1 0 0 1
1 1 1 1 1 1 1 1 1"""

    input3="""7 9
1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 1
1 0 0 0 0 1 1 0 1
1 0 0 0 0 1 0 1 1
1 1 1 1 1 1 1 1 1"""


    input = MakeItAList(input3)

    input = CreateMatrix((50,100), 0.3)


    solids = GetAllSolid(input)
    #print(solids)


    dists = GetDistances(input, solids)
    

    #for di in dists:
    #    print(di)
 



    DebugGrid(solids, input)

    print( max(dists))

    # * hey look! it works with that now
    demi_len = max(dists)[0] - 0.5

    mhm = math.ceil(demi_len*2)
    # ^ ceil handles all the stuff coming from the angles, that's pretty weird tho, like why, it can spin tf




    print(mhm)





main()














#oeeeeee reimplementer les bords mais la technique a l'air d'etre la
# faut math.ceil a la fin de tout du coup apparemment




