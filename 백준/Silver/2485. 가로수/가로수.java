import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] pos = IntStream.range(0, n)
							.map(i -> sc.nextInt())
							.toArray();
		int[] gaps = IntStream.range(0, n-1)
							.map(i -> pos[i + 1] - pos[i])
							.toArray();

		int gcd = IntStream.of(gaps)
						.reduce((a, b) -> gcd(a, b))
						.getAsInt();

		int result = IntStream.of(gaps)
			.map(gap -> gap / gcd - 1)
			.sum();

		System.out.println(result);
	}

	static int gcd(int a, int b) {
		while (b != 0) {
			int t = b;
			b = a % b;
			a = t;
		}
		return a;
	}
}
