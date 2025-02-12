import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int [][] pattern = {
                {1,2,3,4,5},
                {2,1,2,3,2,4,2,5},
                {3,3,1,1,2,2,4,4,5,5}
        };

        int[] score = new int[3];
        List<Integer> list = new ArrayList<Integer>();

        for (int i = 0; i < answers.length; i++) {
            if (pattern[0][i%pattern[0].length] == answers[i]) {
                score[0]++;
            }
            if (pattern[1][i%pattern[1].length] == answers[i]) {
                score[1]++;
            }
            if (pattern[2][i%pattern[2].length] == answers[i]) {
                score[2]++;
            }
        }

        int maxScore = Arrays.stream(score).max().getAsInt();

        for (int i = 0; i < 3; i++) {
            if (maxScore == score[i]) {
                list.add(i+1);
            }
        }
        return list.stream().mapToInt(i -> i).toArray();
    }
}