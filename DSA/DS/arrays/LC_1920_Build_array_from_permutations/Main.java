import java.util.Scanner;
import java.util.Arrays;

class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);

		// input length and list of integers
		int len = scan.nextInt();
		int[] data = new int[len];
		for (int i=0; i<len; i++){
			data[i]=scan.nextInt();
		}
		

		// new answer array
		int[] ans = new int[len];
		for (int i=0; i<len; i++){
			ans[i] = data[data[i]];
		}

		// output display
		System.out.println(Arrays.toString(ans));
	}
}
