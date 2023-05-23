import java.util.Scanner;
import java.util.Arrays;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    int[] arr = new int[n];
    for (int i=0; i<n; i++){
      arr[i] = scan.nextInt();
    }
    int k = scan.nextInt();
    // int n = 4;
    // int[] arr = {4,3,2,1};
    // int k = 2;
    int count=0;
    while(count!=k){
    for (int i=0;i<arr.length-1;i++){
      if (arr[i]>arr[i+1]){
        int temp = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp;
      }
    }
      count++;
    }
    System.out.println(arr[arr.length-k]);
  }
}
