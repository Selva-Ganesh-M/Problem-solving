package com.problems;

public class Print_X_Pattern {
    public static void method(String s){
        for(int i=0; i<s.length(); i++){
            for(int j=0; j<s.length(); j++){
                if (j==i || j==s.length()-i-1){
                    System.out.print(s.charAt(j));
                }
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
