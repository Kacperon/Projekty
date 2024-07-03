from egz1btesty import runtests

def planets( D, C, T, E ):
    E+=1
    n=len(D)
    inf=float("inf")
    F=[[inf]*E for _ in range(n)]
    for b in range (E):
        F[0][b]=b*C[0]
    if E==6:
        print("XD")
    for i in range(1,n):
        for b in range(E):
            j=i-1
            min_cena=inf
            while D[i]-D[j]<=E and j>=0:
                if b+(D[i]-D[j])<E:
                    min_cena=min(min_cena,F[j][b+(D[i]-D[j])])
                j-=1
            for j in range(0,n):
                if T[j][0]==i:
                    min_cena=min(min_cena,F[j][b]+T[j][1])
            if D[i]-D[i-1]<E:
                min_cena=min(min_cena,F[i-1][D[i]-D[i-1]]+b*C[i])
            if D[i]-D[i-1]<E:
                min_cena=min(min_cena,F[i-1][E-1]+(D[i]-D[i-1])*C[i])


            F[i][b]=min_cena



    return min(F[n-1][j] for j in range(E))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
