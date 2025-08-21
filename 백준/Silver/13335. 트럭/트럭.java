import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] trucks = new int[n];

        for (int i = 0; i < n; i++) {
            trucks[i] = Integer.parseInt(st.nextToken());
        }

        Queue<Integer> bridge = new ArrayDeque<>();
        for (int i = 0; i < w; i++) bridge.add(0);

        int time = 0;
        int onBridge = 0;
        int idx = 0;

        while (idx < n) {
            time ++;
            onBridge -= bridge.poll();

            if (onBridge + trucks[idx] <= L) {
                bridge.add(trucks[idx]);
                onBridge += trucks[idx];
                idx++;
            } else {
                bridge.add(0);
            }
        }

        System.out.println(time + w);
    }
}