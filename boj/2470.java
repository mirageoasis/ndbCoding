import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int number = Integer.parseInt(br.readLine());
        Long[] arr = Arrays.stream(br.readLine().split(" "))
                .map(Long::valueOf)
                .sorted(  Comparator.comparingLong(Math::abs))
                .toArray(Long[]::new);

        
        Long mini = 1000000000000000L;

        //System.out.println(Arrays.asList(arr));

        Long a = arr[0];
        Long b = arr[1];

        for (int i = 1; i < arr.length; i++) {
            Long t = Math.abs(arr[i - 1] + arr[i]);
            if (t < mini) {
                a = arr[i - 1];
                b = arr[i];
                mini = Math.abs(t);
            }
        }

        bw.write(Math.min(a, b) + " " + Math.max(a, b) + "\n");
        bw.close();
    }
}