import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int boardSize = sc.nextInt();
        int orderCount = sc.nextInt();

        int x = 0, y = 0;
        int dir = 0; // 0: 동, 1: 남, 2: 서, 3: 북

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, -1, 0, 1};

        boolean isValid = true;

        for (int i = 0; i < orderCount; i++) {
            String cmd = sc.next();
            int v = sc.nextInt();

            if (cmd.equals("TURN")) {
                if (v == 0) {
                    dir = (dir + 3) % 4;
                } else {
                    dir = (dir + 1) % 4;
                }
            } else if (cmd.equals("MOVE")) {
                int nx = x + dx[dir] * v;
                int ny = y + dy[dir] * v;

                if (nx < 0 || ny < 0 || nx > boardSize || ny > boardSize) {
                    isValid = false;
                    break;
                }

                x = nx;
                y = ny;
            }
        }

        if (isValid) {
            System.out.println(x + " " + y);
        } else {
            System.out.println(-1);
        }

        sc.close();
    }
}
