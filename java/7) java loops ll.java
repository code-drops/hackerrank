import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        int s=0;
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            for(int j=0;j<=n-1;j++){
                s=a;
                for(int k=0;k<=j;k++){
                    s = s + ((int)Math.pow(2,k))*b;
                }
                System.out.print(s + " ");
            }
            System.out.println();
        }
        in.close();
    }
}
