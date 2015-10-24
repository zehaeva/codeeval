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
            int n = Integer.parseInt(line);
            System.out.println(f(n));
        }
    }
    
    public static int f(int n) {
        if (n == 0) {
            return 0;
        }
        else if (n == 1) {
            return 1;
        }
        else {
            return f(n-1) + f(n-2);
        }
    }
}
