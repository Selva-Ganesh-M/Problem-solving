import java.util.Arrays;
class Main{
  public static void main(String[] args){
    int[] arr = {10 ,9, 8, 7, 8, 6, 5, 4, 3, 2, 1};
    int len = arr.length;
    for (int i=0; i<len; i++){
      for (int j=i+1; j<len; j++){
        if (arr[i]>arr[j]){
          int temp = arr[i];
          arr[i] = arr[j];
          arr[j] = temp;
        }
      }
    }
    System.out.println(Arrays.toString(arr));
  }
}
