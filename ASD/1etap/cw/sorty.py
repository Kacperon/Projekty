T=[5,11,6,7,2,3,None,None,None,None]
#kopiec
def parent(i):
    return i//2
def left(i):
    return 2*i
def right(i):
    return 2*i+1
def insert(T,v):



    i=T[0]+1
    T[0]+=1
    j=parent(i)
    while i>1 and v>T[j]:
        T[i]=T[j]
        i=j
        j=parent(i)
    T[i]=v
    return T



t=[(1,2),(3,4)]
print(t[0][1])


