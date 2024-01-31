
Implementation of Sorting Algorithms : 

---------------------------------------------axm9415------------------------------------------------------------------>

#Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


Correctness of Selection Sort : 

Correctness Argument for Selection Sort:
Selection sort works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first unsorted element. 
This process continues until the entire array is sorted. The correctness of selection sort can be argued based on the following points:

1. Loop - Invariant: At the beginning of each iteration, the prefix of the array (from the beginning up to the current position) is sorted.
2. Termination: The algorithm terminates when the entire array is sorted, as it consistently selects the smallest unsorted element and moves it to the correct position.
3. Swap Operations: Selection sort only swaps elements once the minimum element is found, ensuring that each element is in its final sorted position.
4. Holistic Approach : Selection sorts only after finding the minimum element in that array and repeats it again and again for the least minimum element from the leftover unsorted array which basically defines holistic approach as it is ensuring to identify the condition first and then sort so that sorting happens in the most proficient manner.


Benchmark specs for my Machine : 

  Model Name:	MacBook Air
  Model Identifier:	Mac14,15
  MacOS : Sonoma Version 14.0
  Memory:	8 GB
  Storage : MacintoshHD 245.11 GB
  Model Number:	MQKU3LL/A
  Chip:	Apple M2
  Total Number of Cores:	8 (4 performance and 4 efficiency)
  Memory:	8 GB
  System Firmware Version:	10151.1.1
  OS Loader Version:	10151.1.1
  Memory:	8 GB
  Type:	LPDDR5
  Manufacturer:	Hynix
  Capacity:	245.11 GB (245,107,195,904 bytes)

Benchmarking results for the runtime of each algorithm : 

Format
A[Size] = .s

Bubble Sort
A[1500] = 0.0943s
A[500] = 0.0087s
A[50] = 0.0001s

Insertion Sort
A[1500] = 0.0357s
A[500r] = 0.0037s
A[50] = 0.0000s

Selection Sort
A[1500] = 0.0386s
A[500r] = 0.0046s
A[50] = 0.0000s










