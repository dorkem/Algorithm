import java.io.IOException;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        String isbn = input.nextLine();

        int starIdx = isbn.indexOf('*');
        int weight = (starIdx % 2 == 0) ? 1 : 3;

        int sum = IntStream.range(0, 13)
                .filter(i -> isbn.charAt(i) != '*')
                .map(i -> (isbn.charAt(i) - '0') * (i % 2 == 0 ? 1 : 3))
                .sum();

        int answer = IntStream.range(0, 10)
                .filter(n -> (sum + n * weight) % 10 == 0)
                .findFirst()
                .getAsInt();

        System.out.println(answer);
    }
}