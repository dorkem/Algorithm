import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int i = 0;
        int j = n-1;
        int count = 0;

        while (i < j){
            if (arr[i] + arr[j] < m){
                i++;
            }
            else if (arr[i] + arr[j] == m){
                count++;
                i++;
                j--;
            }
            else{
                j--;
            }
        }

        System.out.println(count);
        br.close();
    }
}
