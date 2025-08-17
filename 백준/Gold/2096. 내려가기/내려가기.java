import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] maxDP = new int[3];
        int[] minDP = new int[3];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 3; i++) {
            int num = Integer.parseInt(st.nextToken());
            maxDP[i] = num;
            minDP[i] = num;
        }

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            int prevMax0 = maxDP[0], prevMax1 = maxDP[1];
            int prevMin0 = minDP[0], prevMin1 = minDP[1];

            maxDP[0] = a + Math.max(prevMax0, prevMax1);
            maxDP[1] = b + Math.max(Math.max(prevMax0, prevMax1), maxDP[2]);
            maxDP[2] = c + Math.max(prevMax1, maxDP[2]);

            minDP[0] = a + Math.min(prevMin0, prevMin1);
            minDP[1] = b + Math.min(Math.min(prevMin0, prevMin1), minDP[2]);
            minDP[2] = c + Math.min(prevMin1, minDP[2]);
        }

        int maxResult = Math.max(Math.max(maxDP[0], maxDP[1]), maxDP[2]);
        int minResult = Math.min(Math.min(minDP[0], minDP[1]), minDP[2]);

        System.out.println(maxResult + " " + minResult);
    }
}