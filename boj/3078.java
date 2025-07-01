import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, k;
    static String[] list;
    static Map<Integer, Integer> map;

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] t= br.readLine().split(" ");
        n = Integer.parseInt(t[0]);
        k = Integer.parseInt(t[1]);
        list=new String[n];
        map = new HashMap<>();
        long ans = 0;
        for(int i = 0; i < n; i++){
            list[i] = br.readLine();
        }

        for (int i = 0; i < n; i++) {
            int len = list[i].length();
            ans += map.getOrDefault(len, 0);
            map.put(len, map.getOrDefault(len, 0) + 1);
            if (i >= k) {
                int rmLen = list[i - k].length();
                map.put(rmLen, map.get(rmLen) - 1);
            }
        }

        System.out.println(ans);
    }

    public static void main(String[] args) throws Exception {
        solution();
    }
}

