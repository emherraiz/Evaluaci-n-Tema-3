
matrizx = [[1,1],[1,2]]



def determinante(A):
    if len(A) == 1:
        return A[0]

    elif len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1] * A [1][0]

    else:
        for i in range(0, len(A)):
            total += ((-1)**i)*A[0][i]*determinante(A[i])
A = [[1, 2, 3, 4],[1, 2, 3, 4],[2,3,4,1],[5,7,3,4]]
print(pow((-1), (2+1)))
#print(determinante(A))
