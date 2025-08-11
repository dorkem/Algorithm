import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        while(true){
            int w = sc.nextInt();
            int h = sc.nextInt();

            if(w==0 || h==0){
                break;
            }

            int[][] map = new int[h][w];
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    map[i][j] = sc.nextInt();
                }
            }

            int ans = solve(map, w, h);
            System.out.println(ans);
        }
    }

    public static int solve(int[][] map, int w, int h) {
        boolean[][] visited = new boolean[h][w];
        int isLands = 0;
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                if(map[y][x] == 1 && !visited[y][x]){
                    bfs(y , x, map, visited, w, h);
                    isLands++;
                }
            }
        }
        return isLands;
    }

    public static void bfs(int sy, int sx, int[][] map, boolean[][] visited, int w, int h) {
        final int[] dy = {-1, -1, -1, 0, 0, 1, 1, 1};
        final int[] dx = {-1, 0, 1, -1, 1, -1, 0, 1};

        ArrayDeque<int[]> q = new ArrayDeque<>();
        visited[sy][sx] = true;

        q.add(new int[]{sy, sx});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int y = cur[0];
            int x = cur[1];

            for (int dir = 0; dir < 8; dir++){
                int ny = y + dy[dir];
                int nx = x + dx[dir];

                if(0 <= ny && ny < h && 0 <= nx && nx < w){
                    if(!visited[ny][nx] && map[ny][nx] == 1){
                        visited[ny][nx] = true;
                        q.add(new int[]{ny, nx});
                    }
                }
            }
        }
    }
}
