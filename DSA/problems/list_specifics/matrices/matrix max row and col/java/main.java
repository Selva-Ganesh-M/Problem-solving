import java.util.Scanner;
import java.util.Arrays;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int r = scan.nextInt();
    int c = scan.nextInt();
    int[][] mat = new int[r][c];
    for (int i=0; i<r; i++){
      for (int j=0;j<c;j++){
        mat[i][j] = scan.nextInt();
      }
    }
    int[][] arr = rcSums(mat, r, c);
    int[] rs = arr[0];
    int[] cs = arr[1];

    String l1 = "The Sum of rows is";
    for (int i: rs){
      l1+=" ";
      l1+=Integer.toString(i);
    }

    System.out.println(l1);
    
    int maxRP = 0;
    int maxRV = rs[0];
    for (int i=0; i<rs.length; i++){
      if (rs[i]>maxRV) {
        maxRV = rs[i];
        maxRP = i;
      }
    }

    System.out.println(String.format("Row %d has the maximus sum", maxRP+1));
    
    String l2 = "The Sum of columns is";
    for (int i: cs){
      l2+=" ";
      l2+=Integer.toString(i);
    }

    System.out.println(l2);
    
    int maxCP = 0;
    int maxCV = rs[0];
    for (int i=0; i<cs.length; i++){
      if (cs[i]>maxCV) {
        maxCV = cs[i];
        maxCP = i;
      }
    }
    System.out.println(String.format("Column %d has the maximum sum", maxCP+1));
    
  }

  
  static int[][] rcSums(int[][] mat, int r, int c){
    int[] rowSums = new int[r];
    int[] colSums = new int[c];
    int itr = 0;
    for (int i=0; i<r; i++){
      int rs = 0, cs = 0;
      for (int j=0;j<c;j++){
        rs = rs + mat[i][j];
        cs = cs + mat[j][i];
      }
      rowSums[itr]=rs;
      colSums[itr]=cs;
      itr++;
    }
    // int[][] ans = {rowSums, colSums};
    // for (int[] i: ans){
    //   System.out.println(Arrays.toString(i));
    // }
    return ans;
    }
}
