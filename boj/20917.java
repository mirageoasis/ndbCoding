import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Main {

    static int t;
    static int n, m;
    static int[] arr;

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.valueOf(br.readLine());

        for(int l = 0; l < t; l++){
            String[] t = br.readLine().split(" ");
            n = Integer.valueOf(t[0]);
            m = Integer.valueOf(t[1]);
            t = br.readLine().split(" ");
            arr = new int[n];

            for(int i = 0; i < n; i++){
                arr[i] = Integer.valueOf(t[i]);
            }
            Arrays.sort(arr);

            int start = 0;
            int end = arr[arr.length-1] - arr[0] + 1;
            int ans = 0;

            while(start < end){
                int mid = (start+end) / 2;
                int res = 1;
                int last = arr[0];
                for(int i = 1; i < n; i++){
                    if(arr[i] - last >= mid){
                        res+=1;
                        last=arr[i];
                    }
                }
                //System.out.println(res + " " + mid + " " + start + " " + end);
                if (res >= m){
                    ans = Math.max(ans, mid);
                    start=mid+1;
                }else{
                    end=mid;
                }
            }
            System.out.println(ans);
        }


    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

