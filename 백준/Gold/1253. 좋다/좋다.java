import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int count = 0;

        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        for (int i = 0; i < n; i++) {
            long find = arr[i];
            int start = 0;
            int end = n - 1;
            while (start < end){
                if (arr[start] + arr[end] == find){
                    if(start != i && end != i){
                        count++;
                        break;
                    } else if (start == i){
                        start++;
                    } else if (end == i){
                        end--;
                    }
                } else if (arr[start] + arr[end] < find){
                    start++;
                } else{
                    end--;
                }
            }
        }
        System.out.println(count);
        br.close();
    }
}
