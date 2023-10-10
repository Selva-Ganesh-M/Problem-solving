import ds.Sll;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        Sll sll = new Sll();
        sll.append(10);
        sll.append(20);
        sll.append(30);
        sll.prepend(100);
        sll.prepend(500);
        // sll.print();

        try {
            sll.insert(0, 1000);
            sll.insert(0, 5000);
            sll.insert(4, 0);
            sll.insert(8, 100000);
            sll.print();
            System.out.println();
            
        } catch (IndexOutOfBoundsException e) {
            System.out.println(e.getMessage());
        }

        // try {
        //     sll.removeByValue(1000);
        //     sll.print();
        // } catch (Exception e) {
        //     System.out.println(e.getMessage());
        // }

        try {
            sll.removeByPosition(4);
            sll.print();
            // System.out.println(sll.getTailValue());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        
    }
}
