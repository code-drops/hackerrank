/*

Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.:fine=0) .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine= 15 hackos * (number of days late).  .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, fine = 500 hackos * (number of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 hackos.

*/
import java.io.*;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int d1,d2,m1,m2,y1,y2;
        d2 = scan.nextInt();
        m2 = scan.nextInt();
        y2 = scan.nextInt();
        d1 = scan.nextInt();
        m1 = scan.nextInt();
        y1 = scan.nextInt();
        int fine=0;
        if(y2>y1){
            fine = 10000;
        }else if(y2>=y1 && m2>m1){
            fine = 500 * (m2-m1);
        }else if(y2>=y1 && m2>=m1 && d2>d1){
            fine = 15*(d2-d1);
        }else{
            fine = 0;
        }
        System.out.println(fine);
    }
}
