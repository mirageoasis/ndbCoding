import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.Queue;


public class Main {
    static boolean[]visit;
    static int n;
    static int[]chart;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.valueOf(br.readLine());
        chart=new int[n];
        visit=new boolean[100001];

        String[]tmp = br.readLine().split(" ");
        //초기화
        for(int i = 0; i < n; i++){
            chart[i] = Integer.valueOf(tmp[i]);
        }
        Arrays.fill(visit, false);
        long ans = 0L;
        int left=0;
        int right=0;

        while(true){
            //System.out.println(left + " " + right);
            if(left == chart.length){
                break;
            }

            //겹칠 때 까지
            while(true){
                if(right == chart.length){
                    break;
                }
                if(visit[chart[right]]) break;
                visit[chart[right]]=true;
                right+=1;
            }
            ans += (right-left);
            visit[chart[left]]=false;
            left+=1;
        }

        System.out.println(ans);
    }
}