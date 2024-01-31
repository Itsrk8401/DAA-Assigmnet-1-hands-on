
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

Let's explain the selection sort algorithm step by step:

1. Initialization: 

 - The algorithm starts with an unsorted array.

2. Outer Loop (i): 

 - Iterates through each element of the array from the first element (index 0) to the last element (index n-1), where n is the length of the array.

3. Inner Loop (j):

 - For each iteration of the outer loop, an inner loop is executed.

 - The inner loop starts from the next element after the current element being considered by the outer loop (i+1) and goes up to the last element of the array.

 - The purpose of this inner loop is to find the index of the minimum value in the unsorted portion of the array.

4. Finding the Minimum:

 - Within the inner loop, a variable minIndex is initialized to the current outer loop index (i).

 - For each iteration of the inner loop, if the value at the current index (j) is less than the value at arr[minIndex], minIndex is updated to the current index (j).

5. Swapping:

 - After the inner loop completes, if minIndex is not equal to the outer loop index (i), it means a smaller element than the current one at index i was found.

 - In such a case, the elements at index i and minIndex are swapped, bringing the minimum element to its correct sorted position in the array.

6. Iteration:

 - The outer loop continues this process, moving from left to right through the array, with each iteration placing the next smallest element in its correct sorted position.

7. Completion:

 - After the outer loop completes all iterations, the array is fully sorted in ascending order.

8. Return:

- The sorted array is returned as the final output.

Correctness Argument factors for Selection Sort:
                    
Selection sort works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first unsorted element. 
This process continues until the entire array is sorted. The correctness of selection sort can be argued based on the following factors:

1. Loop - Invariant: At the beginning of each iteration, the prefix of the array (from the beginning up to the current position) is sorted.
2. Termination: The algorithm terminates when the entire array is sorted, as it consistently selects the smallest unsorted element and moves it to the correct position.
3. Swap Operations: Selection sort only swaps elements once the minimum element is found, ensuring that each element is in its final sorted position.
4. Holistic Approach : Selection sorts only after finding the minimum element in that array and repeats it again and again for the least minimum element from the leftover unsorted array which basically defines holistic approach as it is ensuring to identify the condition first and then sort so that sorting happens in the most proficient manner.

Use Cases:

Selection sort can be useful in scenarios where simplicity and ease of implementation are prioritized over performance. It's commonly used in educational contexts to teach sorting algorithms and in situations where sorting small datasets efficiently is sufficient.
    
Advantages and Limitations for selection sort :

Advantages:

- Simple and easy to understand and implement in JavaScript.

- Requires minimal auxiliary memory.

- Suitable for small datasets or nearly sorted arrays.

Limitations:

- Inefficient for large datasets due to its quadratic time complexity.

- Not suitable for real-time or performance-critical applications.

- The time complexity of selection sort is O(n^2), where n is the number of elements in the array. This means that its performance degrades quadratically with the size of the input array. Despite its simplicity, selection sort is not suitable for large datasets due to its inefficiency.


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










