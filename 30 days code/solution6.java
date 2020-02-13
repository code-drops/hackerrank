/*

Given a string, S , of length N that is indexed from 0 to n-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String, S.

*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        String s ="",s1="",s2="";
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for(int k=1;k<=n;k++){
            s = sc.nextLine();
            s1="";
            s2="";
            int l = s.length();
            for(int i=0;i<l;i=i+2){
                s1 = s1 + s.charAt(i);
            }
            for(int i=1;i<l;i=i+2){
                s2 = s2 + s.charAt(i);
            }
            System.out.println(s1+ " "+s2);
        }
    }
}

