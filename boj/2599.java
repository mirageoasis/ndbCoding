import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[][] = new int[3][2];
        int result[][] = new int[3][2];
        boolean check = true;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 2; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i <= arr[0][0]; i++) {
            result[0][0] = i;   // A학교 남학생과 B학교 여학생이 짝이되는 수
            result[0][1] = arr[0][0] - i;    // 남아있는 A학교 남학생과 C학교 여학생이 짝이 되는 수
            result[1][1] = arr[2][1] - result[0][1];
            result[1][0] = arr[1][0] - result[1][1];
            result[2][0] = arr[0][1] - result[1][0];
            result[2][1] = arr[2][0] - result[2][0];

            if (result[0][0] >= 0 && result[0][1] >= 0 && result[1][0] >= 0
                    && result[1][1] >= 0 && result[2][0] >= 0 && result[2][1] >= 0) {
                System.out.println(1);
                System.out.println(result[0][0] + " " + result[0][1]);
                System.out.println(result[1][0] + " " + result[1][1]);
                System.out.println(result[2][0] + " " + result[2][1]);
                check = false;
                break;
            }
        }
        if (check) {
            System.out.println(0);
        }
    }
}