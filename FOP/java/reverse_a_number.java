import java.util.Scanner;

class Main {
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int num = scan.nextInt(), rev = 0;
    boolean first = true;
    while (num>0){
      rev*=10;
      rev+=num%10;
      num/=10;
    }
    System.out.println(String.format("%d", rev));
  }
}