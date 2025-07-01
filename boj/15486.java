import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;

public class Main {

    static int n;
    static ArrayList<Integer>[] graph;
    static char[] type;
    static int[] cost_map;
    static int[] cost_chart;

    private static void djk(){
        // (pt, dist)
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (int[] a, int[] b)->{
                    return b[1] - a[1];
                }
        );

        pq.add(new int[]{1, 0});

        while(!pq.isEmpty()){
            int[] t = pq.poll();
            int pt = t[0];
            int cost = t[1];
            int new_cost = cost;
            if(type[pt] == 'T'){
                new_cost-=cost_map[pt];
            }else {
                new_cost = Math.max(cost_map[pt], cost);
            }

            if(new_cost < 0)
                continue;
            if(new_cost <= cost_chart[pt])
                continue;
            cost_chart[pt]=new_cost;
            if (pt == n) {
                return;
            }

            for(int elem: graph[pt]){
                if(new_cost > cost_chart[elem])
                    pq.add(new int[]{elem, new_cost});
            }
        }

    }


    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true){
            n = Integer.valueOf(br.readLine());
            if (n == 0){
                return;
            }
            graph = new ArrayList[n+1];
            for(int i = 0; i < n+1; i++){
                graph[i] = new ArrayList<>();
            }
            cost_chart = new int[n+1];
            type = new char[n+1];
            cost_map = new int[n+1];
            Arrays.fill(cost_chart, -1);

            for(int i = 0; i < n; i++){
                String[] t = br.readLine().split(" ");
                String cmd = t[0];
                type[i+1] = cmd.charAt(0);
                int cost = Integer.valueOf(t[1]);
                cost_map[i+1] = cost;

                for(int j = 0; j < t.length - 3; j++){
                    graph[i+1].add(Integer.valueOf(t[j+2]));
                }
                //System.out.println(graph[i+1]);
            }

            djk();
            System.out.println(cost_chart[n] != -1 ? "Yes" : "No");
            //System.out.println(Arrays.toString(cost_chart));



        }



    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

