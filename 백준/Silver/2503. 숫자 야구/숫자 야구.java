import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] questions = new int[N][3];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            questions[i][0] = Integer.parseInt(st.nextToken());
            questions[i][1] = Integer.parseInt(st.nextToken());
            questions[i][2] = Integer.parseInt(st.nextToken());
        }

        int possibleAnswers = 0;

        for (int i = 123; i <= 987; i++) {
            String answerCandidate = String.valueOf(i);

            if (answerCandidate.charAt(0) == '0' || answerCandidate.charAt(1) == '0' || answerCandidate.charAt(2) == '0') continue;
            if (answerCandidate.charAt(0) == answerCandidate.charAt(1) || answerCandidate.charAt(0) == answerCandidate.charAt(2) || answerCandidate.charAt(1) == answerCandidate.charAt(2)) continue;

            boolean isPossible = true;

            for (int j = 0; j < N; j++) {
                String question = String.valueOf(questions[j][0]);

                int qStrikes = questions[j][1];
                int qBalls = questions[j][2];

                int calStrikes = 0;
                int calBalls = 0;

                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        if (k == l && answerCandidate.charAt(k) == question.charAt(l)) {
                            calStrikes++;
                        } else if (k!=l && answerCandidate.charAt(k) == question.charAt(l)) {
                            calBalls++;
                        }
                    }
                }

                if (calStrikes != qStrikes || calBalls != qBalls) {
                    isPossible = false;
                    break;
                }
            }

            if (isPossible) possibleAnswers++;
        }

        System.out.println(possibleAnswers);
    }
}
