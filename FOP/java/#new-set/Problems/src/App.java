import com.DS.Queue.MaxHeap;
import com.problems.*;
import java.lang.Math;

public class App {
    public static void main(String[] args) throws Exception {

        // problems

        // All_Alphabets.checkAllAlphabets("Aabcdefghijklmnopqrstuvwxyz");
        // Print_X_Pattern.method("PROGRAM");
        // Weight_Calc.method(new int[]{10, 36, 54, 89, 12});
        // Find_Too.method("WELCOMETOZOHOCORPORATION");
        // Palindrome.method("awswa");
        // Armstrong.method(370);
        // Anagram.mtd1("qwertyuiopasdfghjklzxcvbnm");

        // DS

        MaxHeap mxHeap = new MaxHeap(9);

        // populating heap
        mxHeap.insertMax(5);
        mxHeap.insertMax(7);
        mxHeap.insertMax(1);
        mxHeap.insertMax(3);
        mxHeap.insertMax(4);
        mxHeap.insertMax(9);
        mxHeap.insertMax(8);
        mxHeap.insertMax(2);
        mxHeap.insertMax(11);

        // polling from heap
        mxHeap.poll();
        mxHeap.print();
    }
}
