package com.problems;

public class Find_Too {
    public static void method(String str){

        // 2d array prep
        int start = 0, end = 5;
        System.out.println(str.length());
        while (end<=str.length()+1){
            String word = (String)str.subSequence(start, end);
            System.out.println(word.contains("too"));
            start = end;
            end+=5;
            System.out.println(end);
        }

    }    
}
