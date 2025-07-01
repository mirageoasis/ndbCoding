import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Main {

    static long n;
    static boolean[] visit;

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        visit=new boolean[100000001];
        long ans = 1;
        long MOD= (long)Math.pow(2, 32);

        // is_prime

        for(int i = 2; i < n + 1; i++){
            if(!visit[i]){
                for(int j = i * 2; j < n + 1; j += i){
                    visit[j]=true;
                }
                long least = i;
                for( ;least < n + 1; least *= i){
                }
                least /= i;
                ans*=least;
                ans%=MOD;
            }
        }

        System.out.println(ans);


    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

