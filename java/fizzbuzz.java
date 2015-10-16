/* Sample code to read in test cases:
*/
import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        String[] temp;
        Integer first;
        Integer second;
        Integer count_to;
        while ((line = buffer.readLine()) != null) {
            temp = line.trim().split(" ");
            first = Integer.parseInt(temp[0]);
            second = Integer.parseInt(temp[1]);
            count_to = Integer.parseInt(temp[2]);
            boolean fizz_or_buzz;
            for (int i = 1;i <= count_to;i++) {
                fizz_or_buzz = false;
                if (i % first == 0) {
                   System.out.print("F");
                   fizz_or_buzz = true;
                }
                if (i % second == 0) {
                   System.out.print("B");
                   fizz_or_buzz = true;
                }
                if (!fizz_or_buzz) {
                   System.out.print(i); 
                }
                System.out.print(" ");
            }
            System.out.print("\n");
        }
    }
}
