import java.util.Scanner;

class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);

		// input: 2 integers form the user.
		System.out.println("Enter two integers to find which one is an armstrong number: ");
		int num1 = scan.nextInt();
		int num2 = scan.nextInt();

		// func call: armstrong
		int ans = armstrong(num1, num2);

		System.out.println(String.format("%d is the armstrong number.",ans));
	}

	static int armstrong(int a, int b){
		return isArmstrong(a) ? a : b;
	}

	static boolean isArmstrong(int num){
		int length = (int) (Math.log10(num)+1);
		int ans = 0;
		while (num>0){
			ans+=Math.pow(num/10, length);
			num/=10;
		}
		return num==ans;
			
	}
}
