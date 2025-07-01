import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;

public class Main {


    static String origin;
    static int[] dp;
    static int INF = 999999999;
    static int n;
    static String[] strings;

    static int[] cal_counter(String target){
        int[] ret = new int[26];

        for(int i = 0; i < target.length(); i++){
            char a = target.charAt(i);
            ret[a - 'a']+=1;
        }
        return ret;
    }

    static boolean chk_valid(int[]first, int[] second){
        for(int i = 0; i < 26; i++){
            if(first[i] != second[i])
                return false;
        }
        return true;
    }

    static int cal_diff(String first, String second){
        int ret = 0;
        for(int i = 0; i < first.length(); i++){
            if (first.charAt(i) != second.charAt(i))
                ret+=1;
        }
        return ret;
    }

    static int cal(int idx){
        if(idx == -1){
            return 0;
        }
        if (dp[idx] != INF){
            return dp[idx];
        }

        dp[idx]=INF+1;
        for(int i = 0; i < n; i++){
            String now_string = strings[i];
            if(now_string.length() - 1 <= idx){
                String origin_sub = origin.substring(idx+1-now_string.length(), idx+1);
                int[] count_origin = cal_counter(origin_sub);
                int[] count_strings = cal_counter(now_string);
                if(chk_valid(count_origin, count_strings)) {
                    int count_diff = cal_diff(origin_sub, now_string);
                    dp[idx] = Math.min(dp[idx], cal(idx-now_string.length()) + count_diff);
                }
            }
        }

        return dp[idx];
    }

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        origin = br.readLine();
        dp = new int[origin.length()];
        Arrays.fill(dp, INF);
        n = Integer.valueOf(br.readLine());
        strings = new String[n];
        for(int i = 0; i < n; i++){
            strings[i] = br.readLine();
        }
        int ans = cal(origin.length()-1);
        System.out.println(ans >= INF ? -1 : ans);

    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

