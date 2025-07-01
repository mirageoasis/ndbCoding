import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Main {

    static boolean[] visit;
    static int[] chart;
    static int n;
    static Map<Integer, Integer> count;

    private static int dfs(int number, int depth){
        visit[number] = true;
        int next = chart[number];
        count.put(number, depth);
        if (count.containsKey(next))
            return depth - count.get(next) + 1;

        if(!visit[next])
            return dfs(next,depth+1);
        return 0;
    }

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());

        for(int i = 0; i < t; i++){
            n = Integer.valueOf(br.readLine());
            int ans=n;
            visit = new boolean[n+1];
            chart = new int[n+1];
            String[] temp = br.readLine().split(" ");
            for(int j = 0; j < n; j++){
                chart[j+1]=Integer.valueOf(temp[j]);
            }

            for(int j = 1; j < n + 1; j++){
                if(!visit[j]){
                    count = new HashMap<>();
                    ans-=dfs(j, 0);
                }
            }

            System.out.println(ans);
        }


    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

