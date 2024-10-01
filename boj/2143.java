import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;


public class Main {
    static boolean[]visit;
    static int t;
    static int[] first;
    static long[] first_acc;
    static int first_len;
    static int[] second;
    static long[] second_acc;
    static int second_len;

    static List<Long> first_arr = new ArrayList<>();
    static List<Long> second_arr = new ArrayList<>();

    public static int lower_bound(List<Long> arr, long target){
        int start = 0;
        int end = arr.size();

        while(start < end){
            int mid = (start + end) / 2;
            if (arr.get(mid) >= target){
                end=mid;
            }else{
                start=mid+1;
            }
        }

        return start;
    }

    public static int upper_bound(List<Long> arr, long target){
        int start = 0;
        int end = arr.size();

        while(start < end){
            int mid = (start + end) / 2;
            if (arr.get(mid) > target){
                end=mid;
            }else{
                start=mid+1;
            }
        }

        return start;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp;
        long ans = 0;
        t = Integer.valueOf(br.readLine());

        first_len=Integer.valueOf(br.readLine());
        first = new int[first_len];
        first_acc = new long[first_len+1];
        tmp = br.readLine().split(" ");
        for(int i = 0; i < first_len; i++){
            first[i]=Integer.valueOf(tmp[i]);
        }
        first_acc[0]=0;
        for(int i = 1; i < first_len+1; i++){
            first_acc[i]=first[i-1]+first_acc[i-1];
        }

        second_len=Integer.valueOf(br.readLine());
        second= new int[second_len];
        second_acc = new long[second_len+1];
        tmp = br.readLine().split(" ");

        for(int i = 0; i < second_len; i++){
            second[i]=Integer.valueOf(tmp[i]);
        }
        second_acc[0]=0;
        for(int i = 1; i < second_len+1; i++){
            second_acc[i]=second[i-1]+second_acc[i-1];
        }


        for(int i=1; i < first_len+1; i++){
            for(int j = 0; j < i; j++){
                first_arr.add(first_acc[i] - first_acc[j]);
            }
        }

        for(int i=1; i < second_len+1; i++){
            for(int j = 0; j < i; j++){
                second_arr.add(second_acc[i] - second_acc[j]);
            }
        }
        Collections.sort(first_arr);
        Collections.sort(second_arr);


        for(Long a: first_arr){
            long target = t - a;
            int left = lower_bound(second_arr, target);
            int right = upper_bound(second_arr, target);

            ans+=(right - left);
        }
        System.out.println(ans);
    }
}