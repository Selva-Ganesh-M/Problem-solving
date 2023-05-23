import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    int arr[] = new int[n];
    for (int i=0;i<n;i++){
      arr[i] = scan.nextInt();
    }

    int swap = 0;
    for (int i=0; i<arr.length; i++){
      int min = i;
      for (int j=i+1; j<arr.length; j++){
        if (arr[j]<arr[min]){
          min = j;
        }
      }
      if (min != i){
      int temp = arr[i];
      arr[i] = arr[min];
      arr[min] = temp;
      swap++;
      }
    }
    System.out.println(swap);
  }
}
