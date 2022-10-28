def Torre_de_Hanoi(n, aguja_inicial, aguja_final, aguja_intermedia):
    if n==1:
        print ("Movemos el disco 1 desde",aguja_inicial,"hasta",aguja_final)
        return
    Torre_de_Hanoi(n-1, aguja_inicial, aguja_intermedia, aguja_final)
    print ("Movemos el disco",n,"desde",aguja_inicial,"a",aguja_final)
    Torre_de_Hanoi(n-1, aguja_intermedia, aguja_final, aguja_inicial)
# Driver code
n = 64
Torre_de_Hanoi(n,'A','B','C')
