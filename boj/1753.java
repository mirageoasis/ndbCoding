import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, v, start;
    static ArrayList<int[]>[] graph;

    static class Node {

        public int start;
        public int end;

        public Node(int start, int end){
            this.start=start;
            this.end=end;
        }

        @Override
        public int hashCode(){
            return Objects.hash(start, end);
        }
        @Override
        public boolean equals(Object o){
            Node n = (Node)o;
            return n.start == this.start && n.end == this.end;
        }
        @Override
        public String toString(){
            return "start: " + start + " end: " + end;
        }
    }

    static Map<Node, Integer> mapper;
    static int[] dist;
    static int INF=99999999;

    private static void djk(int start){
        dist[start] = 0;
        // pt, dist
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (a, b) -> {
                    return a[1] - b[1];
                }
        );
        pq.add(new int[]{start, 0});
        while(!pq.isEmpty()){
            int[] temp = pq.poll();
            int pt = temp[0];
            int value = temp[1];

            for(int[] t: graph[pt]){
                int new_pt = t[0];
                int val = t[1];
                int new_dist = val + value;
                if(new_dist < dist[new_pt]){
                    dist[new_pt] = new_dist;
                    pq.add(new int[]{new_pt, new_dist});
                }
            }
        }


    }

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] t= br.readLine().split(" ");
        n = Integer.valueOf(t[0]);
        v = Integer.valueOf(t[1]);
        start = Integer.valueOf(br.readLine());

        graph = new ArrayList[n+1];
        for(int i = 1; i< n+1; i++){
            graph[i]=new ArrayList<>();
        }
        dist = new int[n+1];
        Arrays.fill(dist, INF);
        mapper = new HashMap<>();

        for(int i = 0;i < v; i++){
            t= br.readLine().split(" ");
            int st = Integer.valueOf(t[0]);
            int end = Integer.valueOf(t[1]);
            int value = Integer.valueOf(t[2]);
            Node n = new Node(st, end);
            if(mapper.getOrDefault(n, INF) > value){
                mapper.put(n, value);
            }
        }

        for(Map.Entry<Node, Integer> tt: mapper.entrySet()){
            Node n = tt.getKey();
            Integer val = tt.getValue();
            graph[n.start].add(new int[]{n.end, val});
        }
        //System.out.println(Arrays.toString(dist));
        djk(start);

        for(int i = 1; i < n+1; i++){
            System.out.println(dist[i] == INF ? "INF" : dist[i]);
        }


    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

