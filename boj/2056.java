import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    static int workNumber;
    static ArrayList<Integer> graph[];
    static int[] topoCount;
    static int[] timeChart;
    static int[] ans;

    static int topo() {
        Queue<Integer> que = new LinkedList<>();

        for(int i = 1; i < workNumber+1; i++){
            if (topoCount[i] == 0)
                que.add(i);
        }

        while (!(que.isEmpty())) {
            int start = que.poll();
            for (Integer p : graph[start]) {
                topoCount[p] -= 1;
                ans[p] = Math.max(ans[start] + timeChart[p], ans[p]);
                if (topoCount[p] == 0) {
                    que.add(p);
                }
            }
        }
        return Arrays.stream(ans).max().getAsInt();
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        workNumber = Integer.parseInt(br.readLine());
        graph = new ArrayList[workNumber + 1];
        topoCount = new int[workNumber + 1];
        timeChart = new int[workNumber + 1];
        ans = new int[workNumber + 1];

        for (int i = 0; i < workNumber + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i < workNumber + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int time = Integer.parseInt(st.nextToken());
            int work = Integer.parseInt(st.nextToken());
            topoCount[i] = work;
            ans[i] = time;
            timeChart[i] = time;

            for (int j = 0; j < work; j++) {
                int preceedWork = Integer.parseInt(st.nextToken());
                graph[preceedWork].add(i);
            }
        }
        // 1번 부터 시작!

        System.out.println(topo());
        bw.close();
    }
}