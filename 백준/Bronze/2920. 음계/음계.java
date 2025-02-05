import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int inCheck = 0;
        int deCheck = 0;
        Scanner sc = new Scanner(System.in);

        for (int i = 1; i <= 8; i++){
            int a = sc.nextInt();
            if(i == a){
                inCheck++;
            }else if(9-i == a){
                deCheck++;
            }
        }
        if (inCheck == 8){
            System.out.println("ascending");
        }else if(deCheck == 8){
            System.out.println("descending");
        }else{
            System.out.println("mixed");
        }
    }
}
