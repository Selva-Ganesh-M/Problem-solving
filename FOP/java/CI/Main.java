import java.util.Scanner;

class Main {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);

		//input values
		System.out.println("Enter the priciple, no of years, rate of interest: ");
		float p = scan.nextFloat();
		int n = scan.nextInt();
		float r = scan.nextFloat();

		float interest = 0;
		for (int i=0; i<n;i++){
			float yearlyInt = interestCalc(p,r);
			p=p+yearlyInt;
			interest+=yearlyInt;
		}

		System.out.println(String.format("The compound interest would be %.2f",interest));
	}


	static float interestCalc(float p, float r){
		return (p*r)/100;
	}
}

