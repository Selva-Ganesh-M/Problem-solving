import java.util.Scanner;
import java.util.Arrays;
class Main
{
  public static void main(String args[])
  {
    //scanner
    Scanner scan = new Scanner(System.in);
    // user input
    int len = scan.nextInt();
    int arr[] = new int[len];
    for (int i=0;i<len;i++){
    	arr[i] = scan.nextInt();
    }
    // output display
    AlternateSort((arr), len);
    for (int i=0;i<len;i++){
    	System.out.print(arr[i]+" ");
    }
  }
  
  // method declaration
  static void AlternateSort(int[] arr, int len){
    boolean desc = true;
    int end = 0;
  	for (int i=len-1; i>=1; i--){
      end++;
    	for (int j=len-1; j>=end; j--){
        	if (desc==true){
            if (arr[j]>arr[j-1]){
                	int temp = arr[j];
                  	arr[j] = arr[j-1];
                  	arr[j-1] = temp;
                }
          }else{
            if (arr[j]<arr[j-1]){
                int temp = arr[j];
                  arr[j] = arr[j-1];
                  arr[j-1] = temp;
              }
          }
        }
      desc = !desc;
    }
  }
}


// 5            
// 5 1 4 7 9
