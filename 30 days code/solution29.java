/*

Given set S={1,2,3,4,5,6 .... N}. Find two integers,A  and B (where A<B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case,&  represents the bitwise AND operator.

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
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        int max;
        int n,k,i,j,value;
        int[] a;
        for (int tItr = 0; tItr < t; tItr++) {
            max = 0;
            n = scanner.nextInt();
            k = scanner.nextInt();
            a = new int[n];
            for(i=0;i<n;i++){
                a[i] = i+1;
            }
            for(i=0;i<n;i++){
                for(j=i+1;j<n;j++){
                    value = a[i]&a[j];
                    if(value < k && value > max){
                        max = value;
                    }
                }
            }
            System.out.println(max);
        }
        scanner.close();
    }
}
