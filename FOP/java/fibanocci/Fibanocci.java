import java.util.Scanner;

class Fibanocci{

	static void fibanocci(int num){
		int a=0, b=1;
		int count = 2;
		System.out.print(a+" "+b+" ");
		while (count<num){
			System.out.print(a+b+" ");
			int s = a+b;
			a=b;
			b=s;
			count++;
		}

	}

	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);

		System.out.println("Enter the length of fibanocci series: ");
		int num = scan.nextInt();

		fibanocci(num);
	}
}
