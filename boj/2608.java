import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    static Map<String, Integer> stringToNumber = new HashMap<>() {{
        put("I", 1);
        put("IV", 4);
        put("V", 5);
        put("IX", 9);
        put("X", 10);
        put("XL", 40);
        put("L", 50);
        put("XC", 90);
        put("C", 100);
        put("CD", 400);
        put("D", 500);
        put("CM", 900);
        put("M", 1000);
    }};
    static Map<Integer, String> numberToString = new HashMap<>() {{
        put(0, "");
        put(1, "I");
        put(2, "II");
        put(3, "III");
        put(4, "IV");
        put(5, "V");
        put(6, "VI");
        put(7, "VII");
        put(8, "VIII");
        put(9, "IX");
        put(10, "X");
        put(20, "XX");
        put(30, "XXX");
        put(40, "XL");
        put(50, "L");
        put(60, "LX");
        put(70, "LXX");
        put(80, "LXXX");
        put(90, "XC");
        put(100, "C");
        put(200, "CC");
        put(300, "CCC");
        put(400, "CD");
        put(500, "D");
        put(600, "DC");
        put(700, "DCC");
        put(800, "DCCC");
        put(900, "CM");
        put(1000, "M");
        put(2000, "MM");
        put(3000, "MMM");
    }};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s1 = br.readLine();
        String s2 = br.readLine();

        int convertedNumber = stn(s1) + stn(s2);
        String convertedString = nts(convertedNumber);

        System.out.println(convertedNumber);
        System.out.println(convertedString);

        bw.close();
    }

    private static String nts(int convertedNumber) {

        int thousand = convertedNumber - convertedNumber % 1000;
        int hundred = convertedNumber % 1000 - convertedNumber % 100;
        int ten = convertedNumber % 100 - convertedNumber % 10;
        int one = convertedNumber % 10;

        return numberToString.get(thousand) + numberToString.get(hundred) + numberToString.get(ten) + numberToString.get(one);
    }

    private static int stn(String s1) {
        String buffer = s1.substring(0, 1);
        int ret = 0;
        for (int i = 1; i < s1.length(); i++) {
            String nowChar = s1.substring(i, i + 1);
            String bufNow = buffer + nowChar;
            if (!stringToNumber.containsKey(bufNow)) {
                ret += stringToNumber.get(buffer);
                buffer = nowChar;
            } else {
                buffer = bufNow;
            }
        }
        ret += stringToNumber.get(buffer);
        return ret;
    }
}