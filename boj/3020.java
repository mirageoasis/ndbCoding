import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

    static int[] up;
    static int[] down;

    public static int binSearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return start;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.valueOf(st.nextToken());
        int H = Integer.valueOf(st.nextToken()); // 석순
        up = new int[N / 2];
        down = new int[N / 2];

        for (int i = 0; i < N; i++) {
            int val = Integer.valueOf(br.readLine());
            if (i % 2 == 1) {
                up[i / 2] = val; // 종유석
            } else {
                down[i / 2] = val; // 석순
            }
        }
        Arrays.sort(up);
        Arrays.sort(down);

        Long mini = 200000L * 500000;

        for (int i = 0; i < H; i++) {
            int downHeight = H - i;

            int upIdx = binSearch(up, i + 1);
            int downIdx = binSearch(down, downHeight);

            mini = Math.min(mini, N - (long)upIdx - downIdx);
        }

        int cnt = 0;
        for (int i = 0; i < H; i++) {
            int downHeight = H - i;

            int upIdx = binSearch(up, i+1);
            int downIdx = binSearch(down, downHeight);

            if ((N - (long)upIdx - downIdx) == mini) {
                cnt += 1;
            }
            // System.out.println(N  upIdx + N - downIdx);
        }

        bw.write(String.valueOf(mini) + " " + String.valueOf(cnt) + "\n");
        bw.newLine();
        bw.flush();
        bw.close();
    }
}