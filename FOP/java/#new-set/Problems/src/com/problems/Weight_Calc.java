package com.problems;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

public class Weight_Calc {

    public static int[][] method(int[] arr){
        int[][] map = new int[arr.length][2];
        int index = 0;
        for (int n: arr){
            double sqrt = Math.sqrt(n);
            int weight = 0;
            if (sqrt - Math.floor(sqrt)==0){
                weight+=5;
            }
            if (n%4==0 && n%6==0){
                weight+=4;
            }
            if (n%2==0){
                weight+=3;
            }
            map[index] = new int[]{n, weight};
            index++;
        }
        Arrays.sort(map, Comparator.comparingDouble(item->item[1]));
      for (int[] map2 : map) {
        System.out.println(Arrays.toString(map2));
        // System.out.println(map2);
      }
        return map;
    }

}
