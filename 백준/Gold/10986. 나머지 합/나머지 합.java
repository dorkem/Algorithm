import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        long[] sum = new long[n];
        long[] c = new long[m];
        long answer = 0;
        sum[0] = sc.nextInt();

        for (int i = 1; i < n; i++) {
            sum[i] = sum[i-1] + sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            int reminder = (int) ( sum[i] % m );
            if (reminder == 0) { answer++; }
            c[reminder]++;
        }

        for (int i = 0; i<m; i++){
            if (c[i] > 1){
                answer += (c[i]*(c[i]-1)/2);
            }
        }
        System.out.println(answer);
    }
}