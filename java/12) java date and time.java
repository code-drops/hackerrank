import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {
    public static String findDay(int month, int day, int year) {
           Calendar cal = Calendar.getInstance();
           cal.set(year,month-1,day);
           int d=cal.get(Calendar.DAY_OF_WEEK);
           if(d-1==0){
               return "SUNDAY";
           }else if(d-1==1){
               return "MONDAY";
           }else if(d-1==2){
               return "TUESDAY";
           }else if(d-1==3){
               return "WEDNESDAY";
           }else if(d-1==4){
               return "THURSDAY";
           }else if(d-1==5){
               return "FRIDAY";
           }else{
               return "SATURDAY";
           }
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
        int month = Integer.parseInt(firstMultipleInput[0]);
        int day = Integer.parseInt(firstMultipleInput[1]);
        int year = Integer.parseInt(firstMultipleInput[2]);
        String res = Result.findDay(month, day, year);
        bufferedWriter.write(res);
        bufferedWriter.newLine();
        bufferedReader.close();
        bufferedWriter.close();
    }
}
