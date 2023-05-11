import java.util.Scanner;

class SI{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		/*
		 * p -> principle amount
		 * n -> number of years
		 * r -> rate of interest
		 */
		System.out.println("Enter the principle amount: ");
		int p = scan.nextInt();
		System.out.println("Enter no of years:");
		int n = scan.nextInt();
		System.out.println("Enter interest rate:");
		float r = scan.nextInt();

		// Interest calculation
		float interest = (p*n*r)/100;

		// Result printing
		System.out.println(String.format("The total interest amount after the end of %d years if %.1f", n, interest));
	}
}
