from random import randint as r
import time
T1=[r(0,1_000_000) for i in range(1_000_000)]
# T2=[r(0,1_000_000) for i in range(1_000_000)]
T2=T1[:]

def zamiana(T,a,b):
    n=len(T)
    if a>b:
        i=find(T,a)
        while i>0 and T[i-1]>b:
            T[i]=T[i-1]
            i-=1
        T[i]=b
    else:
        i=find(T,a)
        while i<n-1 and T[i+1]<b:
            T[i]=T[i+1]
            i+=1
        T[i]=b
    return T

def find(T, a):
    n = len(T)
    left = 0
    right = n - 1
    if a<T[0]:
        return 0
    while left <= right:
        mid = left + (right - left) // 2
        if T[mid] == a:
            return mid
        elif T[mid] < a:
            left = mid + 1
        else:
            right = mid - 1
    if T[mid]>a:
        mid-=1
    return mid

def insertion_sort_range(T, a, b):
    for i in range(a, b+1):
        key = T[i]
        j = i - 1
        while j >= a and T[j] > key:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key

def bable(t,low,high):
    n=len(t)
    flag=True
    while flag:
        flag=False
        for i in range(low, high):
            if t[i]>t[i+1]:
                flag=True
                t[i],t[i+1]=t[i+1],t[i]

def heapify(arr, n, i):
	largest = i
	l = 2*i+1
	r = 2*i+2

	if l < n and arr[i] < arr[l]:
		largest = l
          
	if r < n and arr[largest] < arr[r]:
		largest = r
          
	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i])
		heapify(arr, n, largest)
def heapSort(arr):
	n = len(arr)
     
	for i in range(n // 2, -1, -1):
		heapify(arr, n, i)
          
	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		heapify(arr, i, 0)

def merge(T1,T2):
    j1,j2=0,0
    n1,n2=len(T1),len(T2)
    n=n1+n2
    T3=[0]*n
    i=0
    while j1<n1 and j2<n2:
        if T1[j1]>T2[j2]:
            T3[i]=T2[j2]
            j2+=1
            i+=1
        else:
            T3[i]=T1[j1]
            j1+=1
            i+=1
    for j in range(j1,n1):
        T3[i]=T1[j]
        i+=1
    for j in range(j2,n2):
        T3[i]=T2[j]
        i+=1
    return T3
def merge_sort(T):
    if len(T) <= 1:
        return T
    mid = len(T) // 2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left, right)

def partition(T, low, high):
    pivot = T[high]
    i = low - 1
    for j in range(low, high):
        if T[j] <= pivot:
            i+=1
            (T[i], T[j]) = (T[j], T[i])
    (T[i + 1], T[high]) = (T[high], T[i + 1])
    return i + 1
def quick_sort(T, low, high):
    if low < high:
        if high-low<5:
             insertion_sort_range(T,low,high)
        else:
            pi = partition(T, low, high)
            quick_sort(T, low, pi - 1)
            quick_sort(T, pi + 1, high)
def sort_q(T):
    quick_sort(T,0,len(T)-1)

def sort_liniowy(P,max):
    n=len(P)
    T=[0]*(max+1)
    for i in range(n):
        T[P[i]]+=1
    for i in range(1,max+1):
        T[i]+=T[i-1]
    T2=[0]*(n+1)
    for i in range(n-1,-1,-1):
        T2[T[P[i]]]=P[i]
        T[P[i]]-=1
    return T2[1:]

def partition_(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    i+=1
    A[i],A[r]=A[r],A[i]
    return i
def quicksort_(A,p,r):
     if p<r:
          q=partition_(A,p,r)
          quicksort_(A,p,q-1)
          quicksort_(A,q+1,r)
def sort_q_(A):
     quicksort_(A,0,len(A)-1)

def hoare_partition(T, p, r):
    x = T[(p + r) // 2]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while not T[j] <= x:
            j -= 1
        i += 1
        while not T[i] >= x:
            i += 1
        if i < j:
            T[i], T[j] = T[j], T[i]
        else:
            return j       
def hoare_quicksort(T, p, r):
    if p < r:
        pivot_index = hoare_partition(T, p, r)
        hoare_quicksort(T, p, pivot_index) # w jednym z wywołań nie omijamy pivota, bo jest on już na swoim miejscu
        hoare_quicksort(T, pivot_index + 1, r)
def sort_hoare(T):
     hoare_quicksort(T,0,len(T)-1)

def hoare_quicksort_in(T, p, r):
    if p < r:
        if r-p<10:
             insertion_sort_range(T,p,r)
        else:
            pivot_index = hoare_partition(T, p, r)
            hoare_quicksort(T, p, pivot_index) # w jednym z wywołań nie omijamy pivota, bo jest on już na swoim miejscu
            hoare_quicksort(T, pivot_index + 1, r)


def shellSort(arr):
  n = len(arr)
  gap = n // 2
  while gap > 0:
    j = gap
    while j < n:
      i = j - gap  # This will help in maintaining the gap value
      while i >= 0:
        # If value on the right side is already greater than the left side value
        # We don't do a swap, else we swap
        if arr[i + gap] > arr[i]:
          break
        else:
          arr[i + gap], arr[i] = arr[i], arr[i + gap]
        i = i - gap  # To check the left side also
      j += 1
    gap = gap // 2

# Python3 program to perform basic timSort 
MIN_MERGE = 32
def calcMinRun(n): 
	"""Returns the minimum length of a 
	run from 23 - 64 so that 
	the len(array)/minrun is less than or 
	equal to a power of 2. 

	e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33, 
	..., 127=>64, 128=>32, ... 
	"""
	r = 0
	while n >= MIN_MERGE: 
		r |= n & 1
		n >>= 1
	return n + r 

def insertionSort(arr, left, right): 
	for i in range(left + 1, right + 1): 
		j = i 
		while j > left and arr[j] < arr[j - 1]: 
			arr[j], arr[j - 1] = arr[j - 1], arr[j] 
			j -= 1

def merge(arr, l, m, r): 

	# original array is broken in two parts 
	# left and right array 
	len1, len2 = m - l + 1, r - m 
	left, right = [], [] 
	for i in range(0, len1): 
		left.append(arr[l + i]) 
	for i in range(0, len2): 
		right.append(arr[m + 1 + i]) 

	i, j, k = 0, 0, l 

	# after comparing, we merge those two array 
	# in larger sub array 
	while i < len1 and j < len2: 
		if left[i] <= right[j]: 
			arr[k] = left[i] 
			i += 1

		else: 
			arr[k] = right[j] 
			j += 1

		k += 1

	# Copy remaining elements of left, if any 
	while i < len1: 
		arr[k] = left[i] 
		k += 1
		i += 1

	# Copy remaining element of right, if any 
	while j < len2: 
		arr[k] = right[j] 
		k += 1
		j += 1

def timSort(arr): 
	n = len(arr) 
	minRun = calcMinRun(n) 

	# Sort individual subarrays of size RUN 
	for start in range(0, n, minRun): 
		end = min(start + minRun - 1, n - 1) 
		insertionSort(arr, start, end) 

	# Start merging from size RUN (or 32). It will merge 
	# to form size 64, then 128, 256 and so on .... 
	size = minRun 
	while size < n: 

		# Pick starting point of left sub array. We 
		# are going to merge arr[left..left+size-1] 
		# and arr[left+size, left+2*size-1] 
		# After every merge, we increase left by 2*size 
		for left in range(0, n, 2 * size): 

			# Find ending point of left sub array 
			# mid+1 is starting point of right sub array 
			mid = min(n - 1, left + size - 1) 
			right = min((left + 2 * size - 1), (n - 1)) 

			# Merge sub array arr[left.....mid] & 
			# arr[mid+1....right] 
			if mid < right: 
				merge(arr, left, mid, right) 

		size = 2 * size 


start=time.time()
sort_hoare(T1)
end=time.time()
delta1=end-start
print('czas:',delta1)
print(T1[:5]+T1[100000:100005])

start=time.time()
timSort(T2)
end=time.time()
delta2=end-start
print('czas:',delta2)
print(T2[:5]+T2[100000:100005])
print((delta2/delta1)*100,"%")




