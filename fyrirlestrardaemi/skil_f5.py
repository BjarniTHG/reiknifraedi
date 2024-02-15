import numpy as np

list1 = [3, 2, 8] #a
list2 = [2, 0, 1] #b
list3 = [-2, 1, 5] #c

vector1 = np.array(list1)
vector2 = np.array(list2)
vector3 = np.array(list3)

matrix1 = np.array([2, 4, 7], [3, 4, 8], [4, 6, 9]) #A
matrix2 = np.array([5, 5, 5], [6, 6, 6], [7, 8, 9]) #B

#lidur a
innfeldi = np.dot(vector1, vector2)
Bb = np.dot(matrix2, vector2)
innfeldi_c_Bb = np.dot(vector3, Bb)
c = np.linalg.norm(vector3)
utkoma = innfeldi - innfeldi_c_Bb / (3 * c)

#lidur b
AT = matrix1.T
B_odru = np.dot(matrix2, matrix2)
summa = AT + B_odru
seinni_svigi = vector1 - 2*vector2
nidurstada = np.dot(summa, seinni_svigi)
final = 2 * nidurstada

#lidur c    
determinant = np.linalg.det(matrix1)
inverse = np.linalg.inv(matrix1)

#lidur d
x = np.linalg.solve(matrix1, vector2)