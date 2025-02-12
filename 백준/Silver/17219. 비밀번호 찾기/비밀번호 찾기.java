import java.util.*;

public class Main {
    public static void main(String[] args) {
        Map<String, String> id = new HashMap<>();
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String name = sc.nextLine();
            String[] parts = name.split(" ");
            id.put(parts[0], parts[1]);
        }

        for (int i = 0; i < m; i++) {
            String name = sc.nextLine();
            System.out.println(id.get(name));
        }
    }
}