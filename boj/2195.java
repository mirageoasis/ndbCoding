import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s1 = br.readLine();
        String s2 = br.readLine();

        int start = 0;
        int ans = 0;

        for(int i = 0; i < s2.length(); i++){
            String substr = s2.substring(start, i+1);
            if (!s1.contains(substr)) {
                start=i;
                ans+=1;
            }
        }
        ans+=1;
        System.out.println(ans);
        bw.flush();
        bw.close();
    }
}