from kol1btesty import runtests

def f(T):
    # tu prosze wpisac wlasna implementacje
    bucket=[[] for _ in range(26)]
    for i, word in enumerate(T):
        for c in word:
            bucket[ord(c)-ord('a')].append(i)
    taken=[False]*26
    return 0


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=False )
