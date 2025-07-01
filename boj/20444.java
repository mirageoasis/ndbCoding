import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;

public class Main {

    static long n, m;

    public static boolean binarySearch(){
        long start = 0;
        long end = n / 2;

        while(start<=end){
            long mid = (start+end)/2;
            long res = (n-mid+1)*(mid+1);
            //System.out.println(mid + " " + res);
            if(res == m){
                return true;
            }else if(res > m){
                end=mid-1;
            }else{
                start=mid+1;
            }
        }
        return false;
    }

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[]t = br.readLine().split(" ");
        n=Long.valueOf(t[0]);
        m=Long.valueOf(t[1]);

        System.out.println(binarySearch() ? "YES" : "NO");


    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

