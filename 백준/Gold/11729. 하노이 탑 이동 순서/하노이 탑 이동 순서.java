import java.io.*;
import java.util.Scanner;


public class Main {

    public static StringBuilder stringBuilder = new StringBuilder();

    public static void hanoi(int n, int start, int end, int aux){
        if(n==1){
            stringBuilder.append(start+" "+end+"\n");
            return;
        }
        hanoi(n-1, start, aux, end);
        stringBuilder.append(start + " " + end + "\n");
        hanoi(n-1, aux, end, start);
    }
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        stringBuilder.append((int)(Math.pow(2,n)-1)).append("\n");
        hanoi(n,1, 3, 2);
        System.out.println(stringBuilder);
    }
}
