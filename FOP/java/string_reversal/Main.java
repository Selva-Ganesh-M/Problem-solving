import java.util.Scanner;

class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter the string to be reversed:");
		String str = scan.next();
		String ans = "";
		for (int i=str.length()-1;i>=0;i--){
			ans=ans+str.charAt(i);
		}
		System.out.println(ans);
	}
}
