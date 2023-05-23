import java.util.Scanner;
import java.util.Arrays;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);

    // getting input
    int n = 8;
    // int[] arr = {9,8,7,6,5,4,3,2,1};
    int[] arr = {7,6,10,5,9,2,1,15,7};
    // for (int i=0; i<n; i++){
    //   arr[i] = scan.nextInt();
    // }
    QuickSort(arr, 0, arr.length-1);
    System.out.println(Arrays.toString(arr));
  }

  static void QuickSort(int[] arr, int start, int end){
    if (start>=end){
      return;
    }

    int pivot = start; 
    int i = start;
    int j = end;
    while (i<j){

      while (arr[i]<=arr[pivot]){
        i++;
        if (i==j){
          break;
        }
      }

      while (arr[j]>arr[pivot]){
        j--;
      }

      if(i<j){
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
      i++;
      j--;
      }
    }

    // moving pivot to j
    int temp = arr[j];
    arr[j] = arr[pivot];
    arr[pivot] = temp;
    pivot = j;


    // calling subsequest sortings
    QuickSort(arr, start, pivot-1);
    QuickSort(arr, pivot+1, end);
  }
}
