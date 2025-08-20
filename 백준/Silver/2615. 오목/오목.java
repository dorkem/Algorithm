import java.io.*;

import java.util.StringTokenizer;

public class Main {

    static int[][] board = new int[21][21];

    static int[] dx = {0, 1, 1, -1};

    static int[] dy = {1, 0, 1, 1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        for (int i = 1; i <= 19; i++) {

            st = new StringTokenizer(br.readLine());

            for (int j = 1; j <= 19; j++) {

                board[i][j] = Integer.parseInt(st.nextToken());

            }

        }

        for (int i = 1; i <= 19; i++) {

            for (int j = 1; j <= 19; j++) {

                if (board[i][j] != 0) {

                    int curColor = board[i][j];

                    for (int k = 0; k < 4; k++) {

                        int px = i - dx[k];

                        int py = j - dy[k];

                        if (board[px][py] == curColor) {

                            continue;

                        }

                        int count = 1;

                        int nx = i + dx[k];

                        int ny = j + dy[k];

                        while (nx >= 1 && nx <= 19 && ny >= 1 && ny <= 19 && board[nx][ny] == curColor) {

                            count++;

                            nx += dx[k];

                            ny += dy[k];

                        }

                        

                        if (count == 5){

                            System.out.println(curColor);

                            System.out.println(i + " " + j);

                            System.exit(0);

                        }

                    }

                }

            }

        }

        System.out.println(0);

    }

}