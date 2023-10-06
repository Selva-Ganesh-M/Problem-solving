package com.problems;

public class Armstrong {
    public static void method(int number){
        Integer num = number;
        String strNum = num.toString();
        int answer = 0;
        for (char x: strNum.toCharArray()){
            answer+=Math.pow(Character.getNumericValue(x), strNum.length());
        }
        System.out.println(number == answer);
    }
}
