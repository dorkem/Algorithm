import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        for (int i = 0; i < num; i++) {
            String s = sc.next();
            int sum = 0;
            int ox = 0;
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                if (c == 'O') {
                    ox += 1;
                }else if (c == 'X') {
                    ox = 0;
                }
                sum+=ox;
            }
            System.out.println(sum);
        }
    }
}