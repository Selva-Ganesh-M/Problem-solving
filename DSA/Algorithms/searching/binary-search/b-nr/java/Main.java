class Main{
  public static void main(String[] args){
    int[] arr = {1,1,2,4,5,6,7,8};
    int loc = BinarySearch(arr, 5);
    System.out.println(loc);
  }

  static int BinarySearch(int[] nums, int src){
    int start=0,end=nums.length-1;
    while (start<=end){
    int mid = Math.floorDiv(start+end, 2);
      if (nums[mid]==src){
        return mid;
      }else if(src<nums[mid]){
        end = mid-1;
      }else{
        start = mid+1;
      }
    }
    return -1;
  }
}


