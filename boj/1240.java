import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;
import java.util.Objects;
import java.util.Arrays;

public class Main {

    static int n, m;
    static int[][] chart;

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[]t = br.readLine().split(" ");
        n = Integer.valueOf(t[0]);
        m = Integer.valueOf(t[1]);
        chart=new int[n][n];

        for(int i = 0; i < n; i++){
            Arrays.fill(chart[i], 999999999);
        }

        for(int i = 0; i < n-1; i++){
            t = br.readLine().split(" ");
            int a = Integer.valueOf(t[0]);
            int b = Integer.valueOf(t[1]);
            int d = Integer.valueOf(t[2]);
            chart[a-1][b-1]=d;
            chart[b-1][a-1]=d;
        }

        for(int k = 0; k < n; k ++){
            for(int i = 0; i < n; i ++){
                for(int j = 0; j < n; j ++){
                    if(chart[i][j] > chart[i][k] + chart[k][j]){
                        chart[i][j] = chart[i][k] + chart[k][j];
                    }
                }
            }
        }

        for(int i = 0; i < m; i++){
            t=br.readLine().split(" ");
            int a = Integer.valueOf(t[0]);
            int b = Integer.valueOf(t[1]);
            System.out.println(chart[a-1][b-1]);
        }

    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

