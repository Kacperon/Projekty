#Kacper Feliks
#Mój algorytm działa podobnie do algorytmu sortującgo przez zliczanie
#w pierwszym etapie zlicza punkty po współrzędnych x i y osobno
#następnie zlicza liczbę punktów których współrzedna x i y nie jest dominująca
#a na koniec szuka punktu który nie dominuje najmniejszej liczby punktów
#czyli dominuje najwiecej a nastepnie zwraca:
#liczbę punktów minus liczbę punktów których punkt największy nie dominuje 
#plus jeden ponieważ punkt największy został policzony 2 razy(po X i po Y)
#algorytm przechodzi 3 razy po tablicy długości N więc złożoność to O(N)
from zad3testy import runtests

def dominance(P):
    n=len(P)
    Tx=[0]*(n+1)
    Ty=[0]*(n+1)
    for i in range(n):
        Tx[P[i][0]]+=1 #zliczanie po X
        Ty[P[i][1]]+=1 #zliczanie po Y
    for i in range(n-1,0,-1):#przekształcam tablicę zliczeń na liczbę elementów większych
        Tx[i]+=Tx[i+1] #przekształcam po X
        Ty[i]+=Ty[i+1] #przekształcam po Y
    
    wynik=Tx[P[1][0]]+Ty[P[1][1]] #przypisuję pierwszy wynik
    for i in P:
        curent=Tx[i[0]]+Ty[i[1]]
        if wynik>curent: #szukam elementu z najmniejszą liczbą elementów których nie dominuje
            wynik=curent
    return n-wynik+1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

