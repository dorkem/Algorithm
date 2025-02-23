import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();
        int[] dp = new int[41];
        dp[1] = 1;
        for (int i = 2; i < 41; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        for (int i = 0; i < testCase; i++) {
            int n = sc.nextInt();
            if (n == 0) {
                System.out.println("1 0");
                continue;
            }
            System.out.println(dp[n-1] + " " + dp[n]);

        }
    }
}