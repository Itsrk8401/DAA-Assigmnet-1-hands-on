import java.util.Arrays;
import java.util.*;

public class Main {
  // Utility method to print an array
  public static void printarray(int[] ray) {
    for (int num : ray) {
      System.out.print(num + " ");
    }
    System.out.println();
  }

  // Main method for testing
  // Testing insertion sort
  public static void main(String[] args) {
    int[] ray = { 5, 1, 4, 2, 8 };

    int[] sortedrayInsertion = Sorting_Algorithms.insertionSort(ray.clone());
    System.out.print("Insertion Sort: ");
    Sorting_Algorithms.printarray(sortedrayInsertion);

    int[] sortedraySelection = Sorting_Algorithms.selectionSort(ray.clone());
    System.out.print("Selection Sort: ");
    Sorting_Algorithms.printarray(sortedraySelection);

    int[] sortedrayBubble = Sorting_Algorithms.bubbleSort(ray.clone());
    System.out.print("Bubble Sort: ");
    Sorting_Algorithms.printarray(sortedrayBubble);

    class Sorting_Algorithms {
      // Insertion Sort
      public static int[] insertionSort(int[] ray) {
        int n = ray.length;
        for (int i = 1; i < n; i++) {
          int key = ray[i];
          int j = i - 1;
          while (j >= 0 && key < ray[j]) {
            ray[j + 1] = ray[j];
            j--;
          }
          ray[j + 1] = key;
        }
        return ray;
      }

      // Selection Sort
      public static int[] selectionSort(int[] ray) {
        int n = ray.length;
        for (int i = 0; i < n - 1; i++) {
          int minIdx = i;
          for (int j = i + 1; j < n; j++) {
            if (ray[j] < ray[minIdx]) {
              minIdx = j;
            }
          }
          int temp = ray[minIdx];
          ray[minIdx] = ray[i];
          ray[i] = temp;
        }
        return ray;
      }

      // Bubble Sort
      public static int[] bubbleSort(int[] ray) {
        int n = ray.length;
        for (int i = 0; i < n - 1; i++) {
          for (int j = 0; j < n - i - 1; j++) {
            if (ray[j] > ray[j + 1]) {
              int temp = ray[j];
              ray[j] = ray[j + 1];
              ray[j + 1] = temp;
            }
          }
        }
        return ray;
      }
    }
  }
}


Output : 

Insertion Sort: 1 2 4 5 8 
Selection Sort: 1 2 4 5 8 
Bubble Sort: 1 2 4 5 8
