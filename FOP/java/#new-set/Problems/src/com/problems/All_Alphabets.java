package com.problems;

public class All_Alphabets {
    public static void checkAllAlphabets(String str){
        long ns = str.toLowerCase().chars().filter(ch -> ch >= 'a' && ch<='z').distinct().count();
        System.out.println(ns == 26);
    }
}
