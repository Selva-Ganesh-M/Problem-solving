import java.util.Scanner;

class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);

		// Year input
		System.out.print("Enter the year: ");
		int year = scan.nextInt();

		// leap year calculation
		String ans = isLeap(year);

		// output display
		System.out.println(String.format("The year %d is %s year.", year, ans ));
	}

	static String isLeap(int year){
		if (year%4==0){
			if (year%100==0){
				if (year%400==0){
					return "leap";
				}
			}else{
				return "leap";
			}
		}
		return "no leap";
	}
}
