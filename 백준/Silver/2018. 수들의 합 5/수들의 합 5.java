import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int count = 1;
        int sum = 1;
        int startpoint = 1;
        int endpoint = 1;

        while (endpoint != n){
            if (sum == n){
                count++;
                endpoint++;
                sum += endpoint;
            }else if(sum > n){
                sum -= startpoint;
                startpoint ++;
            }else{
                endpoint ++;
                sum += endpoint;
            }
        }
        System.out.println(count);
    }
}