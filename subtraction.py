'''
    Subtraction algorithm here
    Receive two numbers n and use them to declare a set of arrays that depict the matrix
    Do same for the next matrix
'''
print("Enter the dimentions of the first matrix")
columns = input("\n\nHow many columns?\n")
rows = input("\n\nHow many rows?\n")
print("\n\nYou have specified a ", columns, " by ", rows, " matrix\n")
n = 2
A1 = [1, 2]
A2 = [2, 3]
B1 = [3, 5]
B2 = [4, 6]
C1 = [0, 0]
C2 = [0, 0]
'''============'''
D1 = [7, 3, 9]
D2 = [3, 7, 1]
D3 = [4, 4, 8]
E1 = [3, 5, 9]
E2 = [7, 4, 8]
E3 = [2, 9, 3]
F1 = [0, 0, 0]
F2 = [0, 0, 0]
F3 = [0, 0, 0]
'''============'''
G1 = [0, 7, 3, 9]
G2 = [3, 7, 9, 1]
G3 = [4, 5, 4, 8]
G4 = [8, 8, 9, 3]
H1 = [2, 9, 4, 1]
H2 = [3, 9, 4, 9]
H3 = [2, 1, 9, 6]
H4 = [3, 0, 4, 2]
I1 = [0, 0, 0, 0]
I2 = [0, 0, 0, 0]
I3 = [0, 0, 0, 0]
I4 = [0, 0, 0, 0]
'''============'''
n = 2
for i in range (0, n):
    C1[i] = A1[i] - B1[i]
    C2[i] = A2[i] - B2[i]
'''============'''
n = 3
for i in range (0, n):
    F1[i] = D1[i] - E1[i]
    F2[i] = D2[i] - E2[i]
    F3[i] = D3[i] - E3[i]
'''============'''
n = 4
for i in range (0, n):
    I1[i] = G1[i] - H1[i]
    I2[i] = G2[i] - H2[i]
    I3[i] = G3[i] - H3[i]
    I4[i] = G4[i] - H4[i]
'''============'''
print("\nMatrix A:\n", A1, "\n", A2)
print("\nMatrix B:\n", B1, "\n", B2)
print("\nMatrix D:\n", D1, "\n", D2, "\n", D3)
print("\nMatrix E:\n", E1, "\n", E2, "\n", E3)
print("\nMatrix G:\n", G1, "\n", G2, "\n", G3, "\n", G4)
print("\nMatrix H:\n", H1, "\n", H2, "\n", H3, "\n", H4)
'''============'''
print("\n\nC1 = ", C1, "\nC2 = ", C2)
print("\n\nF1 = ", F1, "\nF2 = ", F2, "\nF3 = ", F3)
print("\n\nI1 = ", I1, "\nI2 = ", I2, "\nI3 = ", I3, "\nI4 = ", I4)
