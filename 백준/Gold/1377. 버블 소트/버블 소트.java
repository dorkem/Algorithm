import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        Data[] data = new Data[n];
        for (int i = 0; i < n; i++) {
            data[i] = new Data(Integer.parseInt(reader.readLine()),i);
        }
        Arrays.sort(data);
        
        int max = 0;
        for (int i = 0; i < n; i++) {
            if(max < data[i].index - i){
                max = data[i].index - i;
            }
        }
        System.out.println(max + 1);
    }
}

class Data implements Comparable<Data> {
    int value;
    int index;

    public Data(int value, int index) {

        this.value = value;
        this.index = index;
    }

    @Override
    public int compareTo(Data o) {
        return this.value - o.value;
    }
}