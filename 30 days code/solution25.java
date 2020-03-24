/*

A prime is a natural number greater than 1that has no positive divisors other than 1 and itself. Given a number,n , determine and print whether it's Prime or Not Prime.

*/

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        
        for(int i = 0; i < T; i++) {
            int n = in.nextInt();
            int count = 0;
            if(n<2)
                System.out.println("Not prime");
            else {
                for(int j = 2; j*j<= n; j++) {
                    if(n % j == 0)
                        count++;
                }
                
                if(count == 0)
                    System.out.println("Prime");
                else
                    System.out.println("Not prime");
            }
        }
    }
}
