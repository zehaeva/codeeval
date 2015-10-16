import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        Integer sum;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            sum = 0;
            for (int i=0;i<line.length();i++) {
                sum += Character.getNumericValue(line.charAt(i));
            }
         System.out.println(sum);
        }
    }
}
