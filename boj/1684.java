import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void temp(Stack<Character> left, Stack<Character> right, char[] a) {
        for (int i = 0; i < a.length; i++) {
            left.push(a[i]);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        br.readLine();
        String[] temp = br.readLine().split(" ");
        ArrayList<Long> real = new ArrayList<>();

        Long[] r = Arrays.stream(temp)
                .map(Long::new)
                .sorted()
                .toArray(Long[]::new);

        if (r.length == 1) {
            bw.write(r[0] + "\n");
        } else {

            for (int i = 1; i < r.length; i++) {
                real.add(r[i] - r[i - 1]);
            }

            BigInteger[] ans = real
                    .stream()
                    .filter(x -> x != 0)
                    .map(BigInteger::valueOf)
                    .toArray(BigInteger[]::new);

            BigInteger gcd = ans[0];

            for (int i = 0; i < ans.length; i++) {
                gcd = gcd.gcd(ans[i]);
            }

            bw.write(gcd + "\n");
        }


        bw.close();
    }
}