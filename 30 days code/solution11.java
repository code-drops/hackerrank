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
        int[][] arr = new int[6][6];
        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }
        int max=0;
        int s=0;
        for(int r=0;r<=3;r++){
            for(int c=0;c<=3;c++){
                s=0;
                for(int i=r;i<=r+2;i++){
                    for(int j=c;j<=c+2;j++){
                        if(((i==r+1)&&(j==c))||((i==r+1)&&(j==c+2))){
                            s += 0 ;
                        }
                        else{
                            s += arr[i][j];
                        }
                    }
                }
                if(max<s){
                    max = s;
                }
            }
        }
        System.out.println(max);
        scanner.close();
    }
}
