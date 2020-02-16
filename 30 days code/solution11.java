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
