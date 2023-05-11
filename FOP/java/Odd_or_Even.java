import java.util.Scanner;
public class Odd_or_Even {
    public static void main (String[] args){
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        System.out.println(num&1);
    }
}