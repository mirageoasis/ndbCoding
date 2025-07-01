import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Main {

    static int n;
    static int[][] chart;
    static int[][][] dp;

    private static int dp(int idx, int white_cnt, int black_cnt){
        if(idx == -1 && white_cnt == 0 && black_cnt == 0){
            return 0;
        }
        if(idx == -1) {
            return -1;
        }
        if(dp[idx][white_cnt][black_cnt] != -1){
            return dp[idx][white_cnt][black_cnt];
        }


        int ret = dp(idx-1, white_cnt, black_cnt);
        if(white_cnt > 0){
            ret = Math.max(ret, dp(idx-1, white_cnt - 1, black_cnt) + chart[idx][0]);
        }

        if(black_cnt > 0){
            ret = Math.max(ret, dp(idx-1, white_cnt, black_cnt - 1) + chart[idx][1]);
        }
        dp[idx][white_cnt][black_cnt] = ret;

        return ret;
    }

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        chart = new int[1000][2];
        String input = "";
        while((input = br.readLine()) != null) {
            if (input.isEmpty()) break;
            String[] t = input.split(" ");
            int black = Integer.parseInt(t[0]);
            int white = Integer.parseInt(t[1]);
            chart[n][0] = black;
            chart[n][1] = white;
            n+=1;
        }
        dp=new int [n][16][16];

        for(int i = 0; i < n; i++){
            for(int  j = 0; j < 16; j++){
                Arrays.fill(dp[i][j], -1);
            }
        }

        System.out.println(dp(n-1, 15, 15));


    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

