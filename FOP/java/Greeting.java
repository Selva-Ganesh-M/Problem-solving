import java.util.Scanner;

class Greeting {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		String name = scan.next();
		System.out.println(String.format("Hello %s", name));
	}	
}
