import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

    static char[][] c;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Integer N = Integer.valueOf(br.readLine());

        c = new char[N][];

        for (int i = 0; i < N; i++) {
            c[i] = br.readLine().toCharArray();
        }

        // 오른쪽
        // 아래쪽
        // 대각선 아래
        String ans = "ongoing";
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < N; col++) {
                if (c[row][col] != '.') {
                    if (row < N - 2) {
                        char a1 = c[row][col];
                        char a2 = c[row + 1][col];
                        char a3 = c[row + 2][col];

                        if (a1 == a2 && a2 == a3) {
                            ans = String.valueOf(c[row][col]);
                            break;
                        }
                    }

                    if (col < N - 2) {
                        char a1 = c[row][col];
                        char a2 = c[row][col + 1];
                        char a3 = c[row][col + 2];
                        if (a1 == a2 && a2 == a3) {
                            ans = String.valueOf(c[row][col]);
                            break;
                        }
                    }

                    if (row < N - 2 && col < N - 2) {
                        char a1 = c[row][col];
                        char a2 = c[row + 1][col + 1];
                        char a3 = c[row + 2][col + 2];
                        if (a1 == a2 && a2 == a3) {
                            ans = String.valueOf(c[row][col]);
                            break;
                        }
                    }

                    if (row < N - 2 && col > 1) {
                        char a1 = c[row][col];
                        char a2 = c[row + 1][col - 1];
                        char a3 = c[row + 2][col - 2];
                        if (a1 == a2 && a2 == a3) {
                            ans = String.valueOf(c[row][col]);
                            break;
                        }
                    }
                }
            }
        }

        bw.write(ans + "\n");
        bw.flush();
        bw.close();
    }
}