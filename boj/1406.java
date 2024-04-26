import java.io.*;
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

        Stack<Character> left = new Stack<>();
        Stack<Character> right = new Stack<>();

        String alphabets = br.readLine();
        int times = Integer.parseInt(br.readLine());

        char[] ch = alphabets.toCharArray();

        temp(left, right, ch);

        for (int i = 0; i < times; i++) {
            char[] a = br.readLine().toCharArray();

            if (a[0] == 'P') {
                left.push(a[2]);
            } else if (a[0] == 'L') {
                if (!left.empty()) {
                    Character t = left.pop();
                    right.push(t);
                }
            } else if (a[0] == 'D') {
                if (!right.empty()) {
                    Character t = right.pop();
                    left.push(t);
                }
            } else if (a[0] == 'B') {
                if (!left.empty()) {
                    left.pop();
                }
            }
        }

        Character[] l = left.toArray(new Character[0]);

        StringBuilder sb = new StringBuilder();

        for (Character character : l) {
            sb.append(character);
        }

        while(!right.empty()){
            sb.append(right.pop());
        }

        bw.write(sb.toString());
        bw.close();
    }
}