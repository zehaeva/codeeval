/* Sample code to read in test cases:
*/
import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            // Process line of input Here
            String[] values = line.split(",", 2);
            int x, n, i;
            i = 0;
            x = Integer.parseInt(values[0]);
            n = Integer.parseInt(values[1]);
            while (x > (n*i)) {
                i++;
            }
            System.out.println((n*i));
        }
    }
}
