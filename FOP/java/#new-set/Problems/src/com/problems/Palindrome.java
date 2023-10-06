package com.problems;

public class Palindrome {
    public static void method(String str){
        String reveresedString = "";
        for (int i=str.length()-1; i>=0; i--){
            reveresedString+=str.charAt(i);
        }
        System.out.println((str.equals(reveresedString))?true:false);
        
    }
}
