def sort(t):
    n=len(t)
    for i in range(1,n):
        j=i-1
        zap=t[i]
        while j>=0 and zap<t[j]:
            t[j+1]=t[j]
            j-=1
        t[j]=zap
    return t                
    
def sort_punkt(P):
    n=len(P)
    Tx=[0]*(n+1)
    Ty=[0]*(n+1)
    for i in range(n):
        Tx[P[i][0]]+=1
        Ty[P[i][1]]+=1
    for i in range(n-1,0,-1):
        Tx[i]+=Tx[i+1]
        Ty[i]+=Ty[i+1]
    T2x=[(0,0)]*(n+1)
    T2y=[(0,0)]*(n+1)
    for i in range(n):
        T2x[Tx[P[i][0]]]=P[i]
        Tx[P[i][0]]-=1
        T2y[Ty[P[i][1]]]=P[i]
        Ty[P[i][1]]-=1
    return T2x,T2y
# T=[(1, 3), (3, 4), (4, 2), (2, 2)]
# print(sort_punkt(T))


def sort_liniowy(P):
    n=len(P)
    T=[0]*(n+1)
    for i in range(n):
        T[P[i]]+=1
    for i in range(1,n):
        T[i]+=T[i-1]
    T2=[0]*(n+1)
    for i in range(n):
        T2[T[P[i]]]=P[i]
        T[P[i]]-=1
    return T2

def sort_liniowy(P,max):
    n=len(P)
    T=[0]*(max+1)
    T2=[0]*(n+1)
    for i in range(n):
        T[P[i]]+=1
    for i in range(1,max+1):
        T[i]+=T[i-1]
    for i in range(n):
        T2[T[P[i]]]=P[i]
        T[P[i]]-=1
    return T2[1:]
# T=[10,9,6,7,6,5,4,3,0,2,1,0]
# print(sort_liniowy(T,10))

def sortNN(A):
    n=len(A)
    B=[0]*n
    C=[0]*n
    for i in range(n): C[A[i]%n]+=1
    for i in range(1,n): C[i]+=C[i-1]
    for i in range(n-1,-1,-1): 
        B[C[A[i]%n]-1]=A[i]
        C[A[i]%n]-=1
    C=[0]*n
    for i in range(n): C[B[i]//n]+=1
    for i in range(1,n): C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        A[C[B[i]//n]-1]=B[i]
        C[B[i]//n]-=1
    return A
# T=[i*i for i in range(1000000,-1,-1)]
# print(len(sortN2(T)))  
