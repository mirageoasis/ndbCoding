import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.stream.Stream;


public class Main {

    static int cityNum;
    static int busNum;
    static ArrayList<int[]>[] arr;
    static int[] dist;
    static Node[] ans;

    static class Node{
        public List<Integer> a;

        public Node(){
            this.a = new ArrayList<>();
        }
    }

    static class Temp implements Comparable<Temp>{
        public int point;
        public int dist;

        public Temp(int point, int dist){
            this.point = point;
            this.dist = dist;
        }

        @Override
        public int compareTo(Temp t){
            return this.dist - t.dist;
        }
    }

    public void dump(){
        for(int i=0; i < arr.length;i++){
            ArrayList<int[]> a = arr[i];
            System.out.print(i + ": ");
            for(int[] k: a){
                System.out.print(Arrays.toString(k) + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        cityNum = Integer.valueOf(br.readLine());
        busNum = Integer.valueOf(br.readLine());

        arr = new ArrayList[cityNum+1];
        dist = new int[cityNum+1];
        ans = new Node[cityNum+1];

        for(int i = 0; i < cityNum+1;i++){
            arr[i]=new ArrayList<>();
            dist[i] = Integer.MAX_VALUE;
            ans[i] =  new Node();
        }

        for(int i = 0; i < busNum;i++){
            String[] in = br.readLine().split(" ");
            int start = Integer.valueOf(in[0]);
            int end = Integer.valueOf(in[1]);
            int cost = Integer.valueOf(in[2]);

            arr[start].add(new int[]{end, cost});
        }
        // 출발, 도착

        //다익스트라

        String[] in = br.readLine().split(" ");
        int start = Integer.valueOf(in[0]);
        int end = Integer.valueOf(in[1]);

        ans[start].a = new ArrayList<>(Arrays.asList(start));
        djk(start, end);
        System.out.println(dist[end]);
        System.out.println(ans[end].a.size());
        for(int i = 0; i < ans[end].a.size(); i++){
            System.out.print(ans[end].a.get(i) + " ");
        }
        System.out.println();
    }

    private static void djk(int start, int end) {
        dist[start] = 0;
        PriorityQueue<Temp> pq = new PriorityQueue<>();
        pq.add(new Temp(start, 0));
        dist[start]=0;

        while(!pq.isEmpty()){
            Temp t = pq.poll();
            int point = t.point;
            int prevDist = t.dist;
            
            if(prevDist > dist[end]) break;
            
            if(prevDist < dist[point]) continue;

            for(int[] a: arr[point]){
                int goP = a[0];
                int newDi = a[1];

                if(newDi + dist[point] < dist[goP]){
                    dist[goP] = newDi + dist[point];
                    ans[goP].a = new ArrayList<>(ans[point].a);
                    ans[goP].a.add(goP);
                    pq.add(new Temp(goP, newDi + dist[point]));
                }
            }
        }
    }
}