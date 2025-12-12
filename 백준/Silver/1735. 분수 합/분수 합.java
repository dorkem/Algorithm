import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] first = Arrays.stream(sc.nextLine().split(" "))
							.mapToInt(Integer::parseInt)
							.toArray();
		int[] second = Arrays.stream(sc.nextLine().split(" "))
							.mapToInt(Integer::parseInt)
							.toArray();

		int numerator = first[0] * second[1] + second[0] * first[1];
		int denominator = first[1] * second[1];

		int g = gcd(numerator, denominator);
		numerator /= g;
		denominator /= g;

		System.out.println(numerator + " " + denominator);
	}

	static int gcd(int a, int b) {
		if (b == 0) return a;
		return gcd(b, a % b);
	}
}
