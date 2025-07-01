import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map;

public class Main {

    static int n;
    static int[] arr;
    static int maxi = -1;
    static Set<Integer> two;
    static Set<Integer> three;
    static Map<Integer, Integer> enemy;

    static int one_min =99999999;
    static int two_min =99999999;
    static int three_min =99999999;

    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        arr = new int[6];
        n = Integer.valueOf(br.readLine());
        String[] t = br.readLine().split(" ");
        for(int i = 0; i < 6; i++){
            arr[i]=Integer.valueOf(t[i]);
            maxi = Math.max(maxi, arr[i]);
            one_min = Math.min(one_min, arr[i]);
        }
        enemy = new HashMap<>();
        two = new HashSet<>();
        three = new HashSet<>();

        if(n == 1){
            System.out.println(arr[0] +arr[1]+ arr[2] + arr[3] + arr[4] + arr[5] - maxi);
            return;
        }

        enemy.put(0, 5);
        enemy.put(5, 0);
        enemy.put(1, 4);
        enemy.put(4, 1);
        enemy.put(2, 3);
        enemy.put(3, 2);

        for(int i = 0; i < 6; i++){
            for(int j = 0; j < 6; j++){
                if (i != j){
                    if(enemy.get(i) != j){
                        two.add(arr[i] + arr[j]);
                    }
                }
            }
        }

        for(int elem: two){
            two_min = Math.min(elem, two_min);
        }

        three.add(arr[0] + arr[1] + arr[2]);
        three.add(arr[0] + arr[1] + arr[3]);
        three.add(arr[0] + arr[3] + arr[4]);
        three.add(arr[0] + arr[2] + arr[4]);

        three.add(arr[5] + arr[1] + arr[2]);
        three.add(arr[5] + arr[1] + arr[3]);
        three.add(arr[5] + arr[3] + arr[4]);
        three.add(arr[5] + arr[2] + arr[4]);


        for(int elem: three){
            three_min = Math.min(elem, three_min);
        }

        long three_edge = three_min * 4L;
        long two_edge = two_min * 4L;

        long one_side = one_min * (long)Math.pow(n - 2, 2) * 5;
        long floor_pillar = (long) one_min * (n - 2) * 4;

        long up_pillar = two_min * (n - 2) * 4L;
        long pillar = two_min * (n - 2) * 4L;
        System.out.println(three_edge + two_edge + one_side + floor_pillar + up_pillar + pillar);
    }


    public static void main(String[] args) throws Exception {
        solution();
    }
}

