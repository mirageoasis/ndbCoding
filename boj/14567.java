import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, e;
    static int[] dp;
    static int[][] input;

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] t= br.readLine().split(" ");
        n = Integer.valueOf(t[0]);
        e = Integer.valueOf(t[1]);
        dp = new int[n+1];
        input = new int[e][2];
        Arrays.fill(dp, 1);

        for(int i = 0; i < e; i++){
            t= br.readLine().split(" ");
            input[i][0] = Integer.valueOf(t[0]);
            input[i][1] = Integer.valueOf(t[1]);
        }

        Arrays.sort(input, (a, b) -> {
            return a[0] - b[0];
        });
        //System.out.println(Arrays.deepToString(input));
        for(int i = 0; i < e; i++){
            int start = input[i][0];
            int end = input[i][1];

            dp[end] = Math.max(dp[start]+1, dp[end]);
        }


        for(int i = 1; i < n+1; i++){
            System.out.print(dp[i] + " ");
        }
        System.out.println();



    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}



