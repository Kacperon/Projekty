from kol1testy import runtests

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def normalize(T):
    unique_elements = list(set(T))
    merge_sort(unique_elements)
    element_to_index = {element: index + 1 for index, element in enumerate(unique_elements)}
    return [element_to_index[element] for element in T]

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result
def maxrank(T):
    normalized_T = normalize(T)
    fenwick_tree = FenwickTree(max(normalized_T))
    max_rank = 0
    for element in normalized_T:
        current_rank = fenwick_tree.query(element - 1)
        max_rank = max(max_rank, current_rank)
        fenwick_tree.update(element, 1)
    return max_rank

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )