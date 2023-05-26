import java.util.Arrays;

class Main{
    public static void main(String[] args){
        char[] nums = {'c', 'f', 'h'};
        char ans = BS(nums, 'i');
        System.out.println(ans);
        
    }
    
    static char BS(char[] nums, char target){
        int start=0, end=nums.length-1;
        while (start<=end){
            int mid = Math.floorDiv(start+end, 2);
            if (Character.compare(target, nums[mid])==0){
                if (mid >= nums.length-1){
                    return nums[0];
                }else {
                    return nums[mid+1];
                }
            }
            else if (Character.compare(target, nums[mid])<0){
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }
        if (start>=nums.length){
            return nums[0];
        }
        return nums[start];
    }

    
}
