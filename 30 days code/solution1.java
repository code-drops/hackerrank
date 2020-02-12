/*

Complete the code in the editor below. The variables i,d,s and  are already declared and initialized for you. You must:

1. Declare 3 variables: one of type int, one of type double, and one of type String.
2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
3. Use the + operator to perform the following operations:
  a.Print the sum of i plus your int variable on a new line.
  b.Print the sum of d plus your double variable to a scale of one decimal place on a new line.
  c.Concatenate s with the string you read as input and print the result on a new line.

*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		
        Scanner scan = new Scanner(System.in);
        int i2;
        double d2 ;
        String s2;
        i2 = scan.nextInt();
        d2 = scan.nextDouble();
        scan.nextLine();
        s2 = scan.nextLine();
        System.out.println(i+i2);
        System.out.println(d+d2);
        System.out.println(s+s2);
        scan.close();
   }
 }
