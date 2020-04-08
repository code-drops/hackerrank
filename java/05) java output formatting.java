// %-15s%03d\n
// % to depict the formatted output
// - to depict the left alignment
// 15 to depict the length of string
// s for string
// 0 to depict the fill character if needed
// 3 to depict the length of integer
// d for integer
// \n for next line
import java.util.Scanner;
public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String s1=sc.next();
                int x=sc.nextInt();
                System.out.printf("%-15s%03d\n",s1,x);
            }
            System.out.println("================================");

    }
}
