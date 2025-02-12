import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int[][] board, int[] moves) {
        List<Integer> basket = new ArrayList<>();
        int count = 0;
        for (int i = 0; i < moves.length; i++) {
            int x = moves[i];
            for (int j = 0; j < board.length; j++) {
                int xy = board[j][x - 1];
                if (xy != 0) {
                    int answer = xy;
                    board[j][x - 1] = 0;

                    if (basket.isEmpty() || basket.get(basket.size() - 1) != answer) {
                        basket.add(xy);
                        break;
                        
                    } else {
                        basket.remove(basket.size() - 1);
                        count++;
                        break;
                    }
                }
            }
        }
        return count*2;
    }
}