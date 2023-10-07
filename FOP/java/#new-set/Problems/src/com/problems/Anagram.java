package com.problems;

public class Anagram {

    private static int gen(String s, int[] arr){
        char [] charArr = s.toCharArray();
        String ans = "";
        int detectedAlphabets = 0;
        for (int i=0; i<charArr.length; i++) {
            char ch = charArr[i];
            int charAscii = (int)ch;

            // convert uppercase to lowercase
            if (65 <= charAscii && charAscii <=90 ){
                // ans+=(char)(charArr[i]+32);
                int loc = charArr[i]+32-97;
                if (arr[loc]!=1){
                    detectedAlphabets++;
                    arr[loc] = 1;
                }
            }
            else if(97 <= charAscii && charAscii <=122){
                // ans+=charArr[i];
                int loc = (int)charArr[i]-97;
                if (arr[loc]!=1){
                    detectedAlphabets++;
                    arr[loc] = 1;
                }
            }
        }
        return detectedAlphabets;
    }

    // presence array
    public static void mtd1(String str){
        int [] arr = new int[26];
        int res = Anagram.gen("$GDaasdalsab1 9798", arr);
        System.out.println(res);
        
        // for
    }
}
