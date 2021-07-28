'''
    Addition algorithm here
    Receive two numbers n and use them to declare a set of arrays that depict the matrix
    Do same for the next matrix
'''
print("Enter the dimentions of the matrices")
columns = input("How many columns?\n")
rows = input("How many rows?\n")
print("You have specified a ", columns, " by ", rows, " matrix")
rowsA, colsA, rowsB, colsB = 2, 2, 2, 2
rowsD, colsD, rowsE, colsE = 3, 3, 3, 3
rowsG, colsG, rowsH, colsH = 4, 4, 4, 4
n = 2
A=[[1,2],[2,3]]
B=[[3,5],[2,3]]
C=[[0,0],[0,0]]
'''============'''
D=[[7,3,9],[3,7,1],[4,4,8]]
E=[[3,5,9],[7,4,8],[2,9,3]]
F=[[0,0,0],[0,0,0],[0,0,0]]
'''============'''
G=[[0,7,3,9],[3,7,9,1],[4,5,4,8],[8,8,9,3]]
H=[[2,9,4,1],[3,9,4,9],[2,1,9,6],[3,0,4,2]]
I=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
'''============'''

'''2x2 Matrix'''
if colsA != colsB or rowsA!= rowsB:
    print("For sum (A+B) to be defined number of rows & columns in A must equal number of rows & columns in B respectively")
else:
    print()
    for row in range(0, rowsA):
        for col in range(0, colsB):
            C[row][col] = 0
            for prod in range(0, colsA):
                C[row][col] = A[row][col] + B[row][col]

print("Matrix A")
for row in A:
    for col in row:
        print(col, end="\t")
    print()
print()

print("Matrix B")
for row in B:
    for col in row:
        print(col, end="\t")
    print()
print()

print("Sum (A+B)")
for row in C:
    for col in row:
        print(col, end="\t")
    print()
print()


'''3x3 Matrix'''
if colsD != colsE or rowsD!= rowsE:
    print("For sum (D+E) to be defined number of rows & columns in D must equal number of rows & columns in E respectively")
else:
    print()
    for row in range(0, rowsD):
        for col in range(0, colsE):
            F[row][col] = 0
            for prod in range(0, colsD):
                F[row][col] = D[row][col] + E[row][col]

print("Matrix D")
for row in D:
    for col in row:
        print(col, end="\t")
    print()
print()

print("Matrix E")
for row in E:
    for col in row:
        print(col, end="\t")
    print()
print()

print("Sum (D+E)")
for row in F:
    for col in row:
        print(col, end="\t")
    print()
print()


'''4x4 Matrix'''
if colsG != colsH or rowsG!= rowsH:
    print("For sum (G+H) to be defined number of rows & columns in G must equal number of rows & columns in H respectively")
else:
    print()
    for row in range(0, rowsG):
        for col in range(0, colsH):
            I[row][col] = 0
            for prod in range(0, colsA):
                I[row][col] = G[row][col] + H[row][col]

print("Matrix G")
for row in G:
    for col in row:
        print(col, end="\t")
    print()
print()

print("Matrix H")
for row in H:
    for col in row:
        print(col, end="\t")
    print()
print()

print("Sum (G+H)")
for row in I:
    for col in row:
        print(col, end="\t")
    print()
print()
