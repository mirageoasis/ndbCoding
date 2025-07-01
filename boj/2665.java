import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;
    static int[][] map;
    static int[][] chart;

    private static void bfs(){
        Deque<int[]> que = new LinkedList<>();
        que.add(new int[]{0, 0, 0});
        int[] d_r = {-1, 1, 0, 0};
        int[] d_c = {0, 0, -1, 1};

        while(!que.isEmpty()){
            int[] temp = que.pollFirst();
            int row = temp[0];
            int col = temp[1];
            int val = temp[2];
            if(chart[row][col] < val)
                continue;
            chart[row][col] = val;

            for(int i = 0; i < 4; i++){
                int new_row = row + d_r[i];
                int new_col = col + d_c[i];

                if(0<=new_row && new_row < n && 0<=new_col && new_col < n){
                    int plus = map[new_row][new_col] == 0 ? 1 : 0;
                    int new_val = plus + val;
                    if (chart[new_row][new_col] > new_val){
                        chart[new_row][new_col] = new_val;
                        que.add(new int[]{new_row, new_col, new_val});
                    }
                }
            }
        }

    }

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());

        map = new int[n][n];
        chart = new int[n][n];

        for(int i = 0; i < n; i++){
            Arrays.fill(chart[i], n*n+1);
        }

        for(int i = 0; i < n; i++){
            String t = br.readLine();
            for(int j = 0; j < n; j++){
                map[i][j] = t.charAt(j) - '0';
            }
        }

        //chart[0][0]=0;

        bfs();
        System.out.println(chart[n-1][n-1]);
//        System.out.println(Arrays.deepToString(chart));

    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

