/*

Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         int max = 0,l=0 ;
         int n = sc.nextInt();
         String binary="",r="";
         
         while(n>=1){
             binary = binary + n%2;
             n=n/2;
         }
         for(int i=binary.length()-1;i>=0;i--){
            r = r + binary.charAt(i);
         }
         for(int i=0;i<binary.length();i++){
             if(binary.charAt(i)=='1'){
                 l++;
             }
             else{
                 l = 0;
             }
             if(max<l){
                 max = l;
             }
         }
         System.out.println(max);
    }
}
