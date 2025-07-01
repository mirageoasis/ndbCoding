import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    // 학생수, 친구관계 수, 돈
    static int n, m, budget;
    static int[] chart;
    static int[] parent;

    private static int parent_find(int target){
        if(target != parent[target])
            parent[target] = parent_find(parent[target]);
        return parent[target];
    }

    private static void union(int first, int second){
        first = parent_find(first);
        second = parent_find(second);

        if (chart[first] < chart[second]){
            parent[second]=first;
        }else{
            parent[first]=second;
        }


    }

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] t = br.readLine().split(" ");
        n = Integer.valueOf(t[0]);
        m = Integer.valueOf(t[1]);
        budget = Integer.valueOf(t[2]);
        t = br.readLine().split(" ");
        chart = new int[n+1];
        parent = new int[n+1];

        for(int i = 0; i < n; i++){
            chart[i+1] = Integer.valueOf(t[i]);
            parent[i+1] = i+1;
        }

        for(int i = 0; i < m; i++){
            t = br.readLine().split(" ");
            int first = Integer.valueOf(t[0]);
            int second = Integer.valueOf(t[1]);
            union(first, second);
        }

        Set<Integer> temp = new HashSet<>();

        for(int i = 1; i < n+1;i++){
            temp.add(parent_find(i));
        }

        int ans = 0;
        for(int elem: temp){
            ans+=chart[elem];
        }

        System.out.println(ans <= budget ? ans : "Oh no");


    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

