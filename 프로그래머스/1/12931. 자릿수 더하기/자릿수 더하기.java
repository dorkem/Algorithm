class Solution {
    public int solution(int n) {
        int answer = 0;
        String num = String.valueOf(n);
        for(String s : num.split("")) {
            answer += Integer.parseInt(s);
        }

        return answer;
    }
}