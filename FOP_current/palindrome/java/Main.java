class Main {

    public static void main(String[] args){
      System.out.println(isPalindrome(121));
    }
  
    static boolean isPalindrome(int x) {
        int nValue = 0;
        int temp = x;
        while (x>0){
            nValue = (nValue * 10) + (x % 10);
            x = Math.floorDiv(x, 10);
        }
        boolean ans = ((nValue==temp) ? true : false );
        return ans;
    }
}
