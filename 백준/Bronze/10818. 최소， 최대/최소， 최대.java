import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Integer> list =
                Arrays.stream(br.readLine().split(" "))
                        .map(Integer::parseInt)
                        .collect(Collectors.toList());
        int min = list.stream().mapToInt(i -> i).min().getAsInt();
        int max = list.stream().mapToInt(i -> i).max().getAsInt();

        System.out.println(min + " " + max);
    }
}
