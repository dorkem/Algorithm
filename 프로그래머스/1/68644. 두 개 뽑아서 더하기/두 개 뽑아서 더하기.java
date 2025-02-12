import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> list = new TreeSet<>();
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                list.add(numbers[j]+numbers[i]);
            }
        }
        
        return list.stream().mapToInt(i->i).toArray();
    }
}