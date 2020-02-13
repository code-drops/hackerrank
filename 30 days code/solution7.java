/*

Given an array,A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Input Format

The first line contains an integer,N  (the size of our array).
The second line contains N space-separated integers describing array A's elements.

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
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }
        for(int i=n-1;i>=0;i--){
            System.out.print(arr[i] + " ");
        }
        scanner.close();
    }
}
