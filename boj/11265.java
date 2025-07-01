import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, tc;
    static int[][] graph;

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] t= br.readLine().split(" ");
        n = Integer.valueOf(t[0]);
        tc = Integer.valueOf(t[1]);
        graph = new int[n][n];
        for(int i = 0; i < n;i++){
            Arrays.fill(graph[i], 2_000_000_000);
        }

        for(int i = 0; i < n; i++){
            t = br.readLine().split(" ");
            for(int j = 0; j < n; j++){
                graph[i][j] = Integer.valueOf(t[j]);
            }
        }

        // start, end -1

        for(int k = 0; k < n; k++){
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }

        for(int i = 0; i < tc; i++){
            t= br.readLine().split(" ");
            int start = Integer.valueOf(t[0]);
            int end = Integer.valueOf(t[1]);
            int target = Integer.valueOf(t[2]);
            if (graph[start-1][end-1] <= target){
                System.out.println("Enjoy other party");
            }else{
                System.out.println("Stay here");
            }
        }
        //System.out.println(Arrays.deepToString(graph));



    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

