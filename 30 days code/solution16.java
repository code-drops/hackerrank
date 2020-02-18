/*

Read a string,S , and print its integer value; if S cannot be converted to an integer, print Bad String.

*/ 
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        try{
            System.out.println(Integer.valueOf(S));
        }
        catch(Exception e){
            System.out.println("Bad String");
        }
    }
}

