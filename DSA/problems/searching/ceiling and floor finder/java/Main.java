class Main{
  public static void main(String[] args){
    int[] arr = {2,4,5,6,8};
    int[] ceilFloor = CeilFloor(arr, -1);
    System.out.println(String.format("Ceiling of the number is %d.",ceilFloor[0]));
    System.out.println(String.format("Floor of the number is %d.",ceilFloor[1]));
  }

  static int[] CeilFloor(int[] nums, int src){
    int start=0,end=nums.length-1;
    while (start<=end){
    int mid = Math.floorDiv(start+end, 2);
    
      if (nums[mid]==src){
        int[] ceilFloor = {nums[mid], nums[mid]};
        return ceilFloor;
      }else if(src<nums[mid]){
        end = mid-1;
      }else{
        start = mid+1;
      }
}
    int ceil;
    if (start>nums.length-1){
        ceil = src+1;
    }else{
        ceil = nums[start];
    }
    int floor;
    if (end<0){
        floor = src-1;
    }else{
        floor = nums[end];
    }
    int[] ceilFloor = {ceil, floor};
    return ceilFloor;
}
}
