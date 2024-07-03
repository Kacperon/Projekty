#Kacper Feliks
from kol3testy import runtests


# Imię i nazwisko: Jan Kowalski

def orchard(T, m):
    n = len(T)
    
    # Initialize DP array with infinity
    DP = [[float('inf')] * m for _ in range(n)]
    DP[0][0] = 1
    DP[0][T[0]%m]=0
    for i in range(1, n):
        apples = T[i]
        for r in range(m):
            
            DP[i][r] = min(DP[i][r], DP[i - 1][r]+1) #zcinamy

            new_r = (r + apples) % m
            DP[i][new_r] = min(DP[i][new_r], DP[i - 1][r])#nie zcinamy
    
    # The result is the minimum number of trees to cut to make the sum of apples divisible by m
    result = DP[n-1][0]
    return result if result != float('inf') else n




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
