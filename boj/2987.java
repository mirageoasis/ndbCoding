import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    static int[][] arr;

    public static float cal(int a0, int a1, int b0, int b1, int c0, int c1) {
        return Math.abs((float) (a0 * (b1 - c1) + b0 * (c1 - a1) + c0 * (a1 - b1))) / 2;
    }

    public static boolean decide(int[][] arr, float wide, int t1, int t2) {
        float w1 = cal(t1, t2, arr[1][0], arr[1][1], arr[2][0], arr[2][1]);
        float w2 = cal(arr[0][0], arr[0][1], t1, t2, arr[2][0], arr[2][1]);
        float w3 = cal(arr[0][0], arr[0][1], arr[1][0], arr[1][1], t1, t2);

//        System.out.println(w1 + " " + w2 + " " + w3);
//        System.out.println(w1 + w2 + w3);

        return wide == (w1 + w2 + w3);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        arr = new int[3][2];

        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        int N = Integer.parseInt(br.readLine());
        int cnt = 0;
        float wide = cal(arr[0][0], arr[0][1], arr[1][0], arr[1][1], arr[2][0], arr[2][1]);

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int t1 = Integer.parseInt(st.nextToken());
            int t2 = Integer.parseInt(st.nextToken());

            if (decide(arr, wide, t1, t2))
                cnt += 1;

        }

        bw.write(String.valueOf(wide));
        bw.newLine();
        bw.write(String.valueOf(cnt));
        bw.flush();
        bw.close();
    }
}