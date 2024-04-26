import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

    public static ArrayList<Integer>[] chart;
    public static HashSet<Integer>[] ans;

    public static void cal(int start, int N) {
        boolean[] visited = new boolean[N + 1];
        Arrays.fill(visited, false);
        Queue<Integer> tmp = new LinkedList<>();

        tmp.add(start);
        while (!tmp.isEmpty()) {
            int t = tmp.remove();
            ans[start].add(t);
            ans[t].add(start);
            for (Integer c : chart[t]) {
                if (!visited[c]) {
                    tmp.add(c);
                    visited[c] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        chart = new ArrayList[N + 1];
        ans = new HashSet[N + 1];

        for(int i = 0; i < N + 1; i++){
            ans[i] = new HashSet<>();
            chart[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int first = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());
            chart[first].add(second);
        }

        for (int i = 1; i < N + 1; i++) {
            cal(i, N);
        }

        for (int i = 1; i < N + 1; i++) {
            bw.write(String.valueOf(N - ans[i].size()) + "\n");
        }
        bw.flush();
        bw.close();
    }
}