import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int row_len, col_len, jump_dist;
    static long[][] dp;
    static long[][] chart;


    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] t= br.readLine().split(" ");
        row_len = Integer.valueOf(t[0]);
        col_len = Integer.valueOf(t[1]);
        jump_dist = Integer.valueOf(t[2]);
        dp=new long[row_len][col_len];
        chart=new long[row_len][col_len];

        for(int i = 0; i < row_len; i++){
            t = br.readLine().split(" ");
            for(int j = 0; j < t.length; j++){
                chart[i][j] = Long.valueOf(t[j]);
            }
        }

        for(int i = 0; i < row_len; i++){
            Arrays.fill(dp[i], -100 * 100 * 100 * 10000L);
        }
        Arrays.fill(dp[0], 0L);

        for(int i = 0; i < row_len; i++){
            for(int j = 0; j < col_len; j++){
                // row
                for(int k = 1; k < jump_dist+1; k++){
                    // col
                    for(int l = -jump_dist; l <= jump_dist; l++){
                        int new_row = i + k;
                        int new_col = j + l;
                        if(0<=new_row && new_row < row_len && 0<= new_col && new_col < col_len && k + Math.abs(l) <= jump_dist){
                            dp[new_row][new_col] = Math.max(chart[i][j] * chart[new_row][new_col] + dp[i][j], dp[new_row][new_col]);
                        }
                    }
                }
            }
        }

        long ans = dp[row_len-1][0];
        for(int i = 0; i < col_len; i++){
            ans=Math.max(ans, dp[row_len-1][i]);
        }
        System.out.println(ans);
    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}


