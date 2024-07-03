def find_min_max_len(A, n):
    min = len(A[n-1])
    max = len(A[n-1])
    for i in range(0, n - 1, 2):
        if len(A[i]) < len(A[i + 1]):
            if len(A[i]) < min:
                min = len(A[i])
            if len(A[i + 1]) > max:
                max = len(A[i + 1])
        else:
            if len(A[i]) > max:
                max = len(A[i])
            if len(A[i + 1]) < min:
                min = len(A[i + 1])
    return min, max

def pos_counting_sort(A, pos):
    n = len(A)
    B = [0] * 26
    res = [None] * n

    for i in range(n):
        B[ord(A[i][pos]) - ord('a')] += 1

    for i in range(1, 26):
        B[i] += B[i - 1]

    for i in range(n - 1, -1, -1):
        B[ord(A[i][pos]) - ord('a')]-=1
        res[B[ord(A[i][pos]) - ord('a')]] = A[i]
        

    return res

def fast_string_sort(T):
    n = len(T)
    if n<2:
        return
    min, max = find_min_max_len(T, n)
    size = max - min + 1
    buckets = [[] for _ in range(size)]
    for word in T:
        buckets[len(word) - min].append(word)
    res = []
    for i in range(size - 1, -1, -1):
        res += buckets[i]
        res = pos_counting_sort(res, i)
    for i in range(n):
        T[i] = res[i]
    n = len(T)
    min, max = find_min_max_len(T, n)
    size = max - min + 1

    buckets = [[] for _ in range(size)]

    for word in T:
        buckets[len(word) - min].append(word)

    res = []

    for i in range(size - 1, -1, -1):
        res += buckets[i]
        res = pos_counting_sort(res, i)

    for i in range(n):
        T[i] = res[i]
T=['dsfsa','bdfs','fsdc','asdfsd','aff','afdf']
fast_string_sort(T)
print(T)