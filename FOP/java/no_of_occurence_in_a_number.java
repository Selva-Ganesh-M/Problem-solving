import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);

    // getting the value
    System.out.println("Enter the value:");
    int num = scan.nextInt();
    int c_num = num;

    // getting the digit to count
    System.out.println("Enter which value to count:");
    int digit = scan.nextInt();

    // count dec
    int count = 0;
    
    // traversing the number to count the occurences
    while (num>0){
      int rem = num%10;
      if (rem==digit){
        count++;
      }
      num = Math.floorDiv(num, 10);
    }

    // printing the count
    System.out.println(String.format("The digit %d is occuring %d times in the given number %d.", digit, count, c_num));
  }
}