import java.io.*;
import java.util.regex.Pattern;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        for(int i = 0; i < N; i++){
            String s = br.readLine();
            Pattern pattern = Pattern.compile("(100+1+|01)+");
            if(pattern.matcher(s).matches()){
                bw.write("YES\n");
            }else{
                bw.write("NO\n");
            }
            bw.flush();
        }
        bw.close();
    }
}