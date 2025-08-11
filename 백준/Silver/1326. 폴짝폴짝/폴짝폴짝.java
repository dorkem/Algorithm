import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        int[] a = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) a[i] = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        int[] dist = new int[N + 1];
        Arrays.fill(dist, -1);

        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(start);
        dist[start] = 0;

        while (!q.isEmpty()) {
            int cur = q.poll();
            if (cur == end) break;

            int step = a[cur];

            for (int next = cur + step; next <= N; next += step) {
                if (dist[next] != -1) continue;
                dist[next] = dist[cur] + 1;
                q.add(next);
            }

            for (int next = cur - step; next >= 1; next -= step) {
                if (dist[next] != -1) continue;
                dist[next] = dist[cur] + 1;
                q.add(next);
            }
        }

        System.out.println(dist[end]);
    }
}