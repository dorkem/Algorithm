import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] trees = new int[N];
        int maxH = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int h = Integer.parseInt(st.nextToken());
            trees[i] = h;
            if (h > maxH) maxH = h;
        }

        int low = 0, high = maxH + 1;
        int answer = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            long cut = 0L;

            for (int h : trees) {
                if (h > mid) cut += (h- mid);
            }
            
            if (cut >= M) {
                answer = mid;
                low = mid + 1;
            }
            
            else {
                high = mid - 1;
            }
        }
        System.out.println(answer);
    }
}