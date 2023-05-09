import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int i=1, fact=1;
    
    System.out.print("Enter you number: ");
    int number = scan.nextInt();

    while (i<=number){
      fact = fact * i;
      i=i+1;
    }

    System.out.println("The factorial is: "+fact);
    
  }
}