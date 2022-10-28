matriz = [[1, 2, 3, 4],[1, 2, 3, 4],[2,3,4,1],[5,7,3,4]]
matrizx = [[1,2],[1,2]]

A = 0
n = len(matrizx)
i = 0


for i in range(n):
    temp = 1
    w = i
    for j in range(n):
        if w == n:
            w = 0
        temp = temp * matrizx[w][j]
        w += 1


    A += temp

print(A)
