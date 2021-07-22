'''
    Multiplication algorithm here
    Receive two numbers n and use them to declare a set of arrays (matrix)
    Do same for the next matrix
'''
print("Enter the dimentions of the first matrix")
n = input("\n\nHow many rows?\n")
p = input("\n\nHow many columns?\n")
print("\n\nYou have specified a ", n, " by ", p, " matrix\n")
'''=========================================================================='''
rowsA, colsA, rowsB, colsB = 5, 4, 4, 3
A=[[7,3,9,1],[3,7,1,7],[4,4,8,6],[7,3,2,4],[3,9,4,8]]
B=[[3,5,9],[7,4,8],[2,9,3],[2,4,8]]
C=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
if colsA != rowsB:
    print("For product (AB) to be defined number of columns in A must equal number of rows in B")
else:
    print("\n\n")
    for row in range(0, rowsA):
        for col in range(0, colsB):
            C[row][col] = 0
            for prod in range(0, colsA):
                C[row][col] += A[row][prod]*B[prod][col]
for row in C:
    for col in row:
        print(col, end="\t")
    print()
