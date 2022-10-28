
matrizx = [[1,1],[1,2]]



def determinante(A):
    if isinstance(A, int):
        det = A
        return det

    det = 0
    fila_1 = A[0][:]
    A[0][:] = []

    for i in range(len(A[0])):
        A_i = A
        A_i[:][i] = []

        det += pow((-1), (i+1)) * fila_1[i] * determinante(A_i)


A = [[2, 8, 3, 4],[2, 2, 3, 4],[2,3,4,1],[5,7,3,4]]
print(isinstance(4, int))
print(pow((-1), (2+1)))
print(determinante(A))
