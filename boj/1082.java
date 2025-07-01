import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;
import java.util.Objects;
import java.util.Arrays;

public class Main {

    static int n;
    static int[] price;
    static String[] dp;
    static int budget;

    static int retZero(String t){
        if (t.isEmpty()){
            return 0;
        }
        int i = 0;
        for(; i < t.length(); i++){
            if (t.charAt(i) != '0'){
                return i;
            }
        }
        return i;
    }

    static boolean cmp(String s1, String s2){
        // if s1 > s2;
        if(!s1.isEmpty()){
            s1 = s1.substring(retZero(s1));
        }
        if(!s2.isEmpty()){
            s2 = s2.substring(retZero(s2));
        }

        if(s1.length() != s2.length()){
            return s1.length() > s2.length();
        }
        return s1.compareTo(s2) > 0;
    }

    static String cal(int nowBudget){
        if (nowBudget == 0){
            dp[0]="";
            return "";
        }

        if(!dp[nowBudget].isEmpty()){
            return dp[nowBudget];
        }
        String ret = "";

        for(int i = 0; i < n; i++){
            String now = String.valueOf(i);
            int now_price = price[i];
            if (nowBudget-now_price >= 0){
                String val = cal(nowBudget-now_price);
                if (val.isEmpty()){
                    if (cmp( now, ret)){
                        ret = now;
                    }
                }else{
                    String front = String.valueOf(val.charAt(0));
                    if(cmp(front, now)){
                        String real_val = val + now;
                        if(cmp(real_val, ret)) {
                            ret = real_val;
                        }
                    }else{
                        String real_val = now + val;
                        if(cmp(real_val, ret)) {
                            ret = real_val;
                        }
                    }
                }
            }
        }
        //System.out.println("ret is: " + ret + " " + "now budget: " + nowBudget);
        dp[nowBudget]=ret;
        return ret;
    }

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        price = new int[n];
        dp = new String[51];
        Arrays.fill(dp, "");

        String[] t = br.readLine().split(" ");
        for(int i = 0; i < n; i++){
            price[i]=Integer.valueOf(t[i]);
        }
        budget = Integer.valueOf(br.readLine());

        System.out.println(!cal(budget).isEmpty() ? cal(budget) : 0);
    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

