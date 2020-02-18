/*

Given a  2D Array,
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
Task : Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

*/
import java.util.Scanner;

public class Day11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int i=0; i < 6; i++){
            for(int j=0; j < 6; j++){
                arr[i][j] = scanner.nextInt();
            }
        }
        
        int sum = 0;
        int max = -1000;
        
        for (int r=0; r<4; r++){
            for (int c=0; c<4; c++){
                sum=0;
                for(int i=r;i<=r+2;i++){
                    for(int j=c;j<=c+2;j++){
                        if(((i==r+1)&&(j==c))||((i==r+1)&&(j==c+2))){
                            sum += 0 ;
                        }
                        else{
                            sum += arr[i][j];
                        }
                    }
                }
                if(max<sum){
                    max = sum;
                }
            }
        }
        scanner.close();
        System.out.println(max);
    }
}
