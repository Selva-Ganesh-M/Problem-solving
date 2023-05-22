class Main{
  public static void main(String [] args){
    int[] arr = {1, 2,3,4,5,6,7,8,9};
    int target=11;
    int len = arr.length;
    int fp=0,lp=len-1;
    System.out.println(BinarySearch(arr, target, fp, lp));
  }

  static int BinarySearch(int[] arr, int target, int fp, int lp){
    if (fp>lp){
      System.out.println("fp > lp");
      return -1;
    }
    int mid=Math.floorDiv(fp+lp, 2);
    if (arr[mid]==target){
      return mid;
    }
    if (target<arr[mid]){
      lp = mid-1;
      return BinarySearch(arr, target, fp, lp);
    }
    if (target>arr[mid]){
      fp = mid+1;
      return BinarySearch(arr, target, fp, lp);
    }
    return -1;
  }
}
