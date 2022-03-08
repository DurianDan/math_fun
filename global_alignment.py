#!usr/bin/python3
#Global Alignment Matrix
#create different penalty for diferent modifications
#compare different sequences to a reference
alphabet = ["A","C","G","T"]
score = [[0,4,2,4,8],\
    [4,0,4,2,8],\
        [2,4,0,4,0],\
            [4,2,4,0,8],\
                [8,8,8,8,8]]            

'''
    A   C   G   T   NULL
A   0   4   2   4   8   
C   4   0   4   2   8
G   2   4   0   4   8
T   4   2   4   0   8
NULL 8  8   8   8   
'''

def GlobalAlignment(x,y):
    Matrix = []
    #initialize matrix of X,Y arrays
    for i in range(len(x)+1):
        Matrix.append([0]*(len(y)+1))

    for i in range(1,len(x)+1):
        Matrix[i][0] = Matrix[i-1][0] + score[alphabet.index(x[i-1])][-1] 
    for i in range(1,len(y)+1):
        Matrix[0][i] = Matrix[i-1][0] + score[-1][alphabet.index(y[i-1])] 

    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            editHor = Matrix[i][j-1] + 8
            editVer = Matrix[i-1][j] + 8
            if x[i-1] == y[j-1]:
                editDiag = Matrix[i-1][j-1]
            else:
                editDiag = Matrix[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
            Matrix[i][j] = min(editDiag,editHor,editVer)
    print(Matrix[-1][-1])

x = "ATCGTAGCTGTGGACGTAGCGAT"
y = "ATCGTAGCTGTGGACGTAGCGAT"
GlobalAlignment(x,y)



