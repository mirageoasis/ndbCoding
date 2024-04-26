import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    static long[] arr;
    static Stack<Long> s;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int number = Integer.parseInt(br.readLine());
        arr = new long[number];
        s = new Stack<>();
        long ans = 0;
        long maxi;

        // 20 10 100 10 5 6 8
        for (int i = 0; i < number; i++)
            arr[i] = Integer.parseInt(br.readLine());
        maxi = arr[0];
        s.push(arr[0]);

        for (int i = 1; i < arr.length; i++) {
            if (s.peek() < arr[i]) {
                ans += arr[i] - s.peek();
            }
            s.pop();
            s.push(arr[i]);
            maxi = Math.max(arr[i], maxi);
        }

        ans += maxi - s.pop();

        System.out.println(ans);
        bw.close();
    }
}