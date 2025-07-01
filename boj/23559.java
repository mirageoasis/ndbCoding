import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Main {

    static int n, budget;

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] t = br.readLine().split(" ");

        n = Integer.valueOf(t[0]);
        budget = Integer.valueOf(t[1]);
        int ans = 0;
        int[][] chart = new int[n][2];
        for(int i = 0; i < n; i++){
            t = br.readLine().split(" ");
            int first = Integer.valueOf(t[0]);
            int second = Integer.valueOf(t[1]);
            chart[i][0] = first;
            chart[i][1] = second;
        }

        Arrays.sort(chart, (a, b)->{return (a[1] - a[0]) - (b[1] - b[0]);});
        int cnt = (budget - 1000 * n) / 4000;
        for(int i = 0; i < n; i++){
            if (chart[i][1] >= chart[i][0]){
                ans+=chart[i][1];
            }else{
                if(cnt > 0){
                    ans+=chart[i][0];
                }else{
                    ans+=chart[i][1];
                }
                cnt-=1;
            }
            //System.out.println(ans);
        }
        System.out.println(ans);
    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

