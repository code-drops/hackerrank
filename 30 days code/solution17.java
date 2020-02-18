/*

Write a Calculator class with a single method: int power(int,int). The power method takes two integers,n  and p, as parameters and returns the integer result of n^p. If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.

*/
import java.util.*;
import java.io.*;
class invalid extends Exception{
    invalid(String S){
        super(S);
    }
}
class Calculator{
    int power(int n,int p) throws invalid{
        if(n<0 || p<0){
            throw new invalid("n and p should be non-negative");
        }
        return (int)Math.pow(n,p);
    }
}
class Solution{

    public static void main(String[] args) {
    
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while (t-- > 0) {
        
            int n = in.nextInt();
            int p = in.nextInt();
            Calculator myCalculator = new Calculator();
            try {
                int ans = myCalculator.power(n, p);
                System.out.println(ans);
            }
            catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
        in.close();
    }
}
