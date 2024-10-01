import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.Queue;


public class Main {

    class A {

        public A() {
        }

        public void print() {
            System.out.println("A");
        }
    }

    static int alpha;
    static boolean beta;
    static ArrayList<Integer>[] gamma;

    static int[][] chart;
    static boolean[][] visit;
    static int row_len;
    static int col_len;
    static int n;
    static ArrayList<Integer>[] arr;
    static int[] arr2;

    static void bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 0});
        visit[0][0] = true;
        chart[0][0] = 0;

        int[] d_r = {1, 1, -1, -1, 2, 2, -2, -2};
        int[] d_c = {2, -2, 2, -2, 1, -1, 1, -1};

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];
            int number = cur[2];

            for (int i = 0; i < 8; i++) {
                int new_r = r + d_r[i];
                int new_c = c + d_c[i];

                if (moveable(new_r, new_c)) {
                    visit[new_r][new_c] = true;
                    chart[new_r][new_c] = number + 1;
                    q.add(new int[]{new_r, new_c, number + 1});
                }
            }

        }
    }

    static class Temp implements Comparable<Temp> {

        int a;
        int b;

        public Temp(int a, int b) {
            this.a = a;
            this.b = b;
        }

        @Override
        public int compareTo(Temp t) {
            if (this.a != t.a) {
                return this.a - t.a;
            }
            return this.b - t.b;
        }

        @Override
        public String toString() {
            return this.a + " " + this.b;
        }

        @Override
        public boolean equals(Object o) {
            Temp t = (Temp) o;
            return this.a == t.a && this.b == t.b;
        }

        @Override
        public int hashCode() {
            return Objects.hash(this.a, this.b);
        }
    }

    static int lower_bound(int[] arr3, int target, int left, int right) {
        while (left < right) {
            //System.out.println(left + " " + right);
            int mid = (left + right) / 2;
            if (arr3[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    static int upper_bound(int[] arr3, int target, int left, int right) {
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr3[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    private static boolean moveable(int row, int col) {
        if (0 <= row && row < row_len && 0 <= col && col < col_len) {
            return !visit[row][col];
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.valueOf(br.readLine());
        arr2 = new int[n];

        String[] s1 = br.readLine().split(" ");

        for (int i = 0; i < s1.length; i++) {
            arr2[i] = Integer.valueOf(s1[i]);
        }

        Arrays.sort(arr2);
        //System.out.println(Arrays.toString(arr2));
        int ans = 0;
        for (int i = 0; i < n; i++) {
            boolean tmp = false;
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }

                int target = arr2[i] - arr2[j];

                int left = lower_bound(arr2, target, 0, arr2.length);
                int right = upper_bound(arr2, target, 0, arr2.length);
                //System.out.println(left + " " + right + " " + i + " " + j + " " + target);
                int cnt = right - left;

                if (left <= i && i < right) {
                    cnt -= 1;
                }

                if (left <= j && j < right) {
                    cnt -= 1;
                }

                if (cnt > 0) {
                    tmp = true;
                    break;
                }
            }
            if (tmp) {
                ans += 1;
            }
            //System.out.println();
        }
        System.out.println(ans);
    }
}