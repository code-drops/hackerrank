import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = "";
        int i=1;
        while(scan.hasNext()){
            s = scan.nextLine();
            if(s.isEmpty()){
                break;
            }
            System.out.println(i+" "+s);
            i++;
        }   
    }
}
