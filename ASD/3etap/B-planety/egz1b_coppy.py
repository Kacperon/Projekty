from egz1btesty import runtests

def planets( D, C, T, E ):
    E+=1
    n=len(D)
    inf=float("inf")
    F=[[inf]*E for _ in range(n)]
    F[0][0]=0

    for i in range(n-1):
        for b in range(1,E):
            F[i][b]=min(F[i][b],F[i][b-1]+C[i])
        if T[i][0]>i:
            F[T[i][0]][0]=min(F[i][0]+T[i][1],F[T[i][0]][0])

        dist=D[i+1]-D[i]
        for b in range(dist,E):
            F[i+1][b-dist]=min(F[i+1][b-dist],F[i][b])
                

        

    return F[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
