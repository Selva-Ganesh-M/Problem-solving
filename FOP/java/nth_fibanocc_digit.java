import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter a number to find nth fibanocci digit:");
    int n = scan.nextInt();
    int p=0, i=1, count=2;
    while (count<n){
      int temp = i;
      i=i+p;
      p = temp;
      count++;
    }
    System.out.println(i);
  }
}