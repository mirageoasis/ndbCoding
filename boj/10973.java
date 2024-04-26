import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;
import java.sql.SQLOutput;
import java.util.*;
import java.util.stream.Stream;

public class Main {

    public static Integer[] arr;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        arr = new Integer[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        if (isFirst()) {
            bw.write("-1\n");
        } else {
            bw.write(cal());
        }

        bw.flush();
        bw.close();
    }

    private static String cal() {
        int idx = 0;
        int rear_max_idx = -1;

        for (int i = 0; i < arr.length - 1; i++)
            if (arr[i] > arr[i + 1])
                idx = i;

        rear_max_idx = idx + 1;

        // idx idx + 1
        for (int i = idx + 1; i < arr.length; i++)
            if (arr[rear_max_idx] < arr[i] && arr[i] < arr[idx]) {
                rear_max_idx = i;
            }

        Integer temp = arr[idx];
        arr[idx] = arr[rear_max_idx];
        arr[rear_max_idx] = temp;

        Integer[] front = Arrays.copyOfRange(arr, 0, idx + 1);
        Integer[] rear = Arrays.copyOfRange(arr, idx + 1, arr.length);
        Arrays.sort(rear, Collections.reverseOrder());
        Integer[] ans = Stream.concat(Arrays.stream(front), Arrays.stream(rear)).toArray(Integer[]::new);

        return String.join(" ", Arrays.stream(ans).map(String::valueOf).toArray(String[]::new));
    }

    private static boolean isFirst() {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != i + 1) {
                return false;
            }
        }
        return true;
    }
}