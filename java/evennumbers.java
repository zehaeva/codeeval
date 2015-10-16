import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        Integer test_me;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            test_me = Integer.parseInt(line);
            if (test_me % 2 == 0) {
                System.out.print("1\n");
            }
            else {
                System.out.print("0\n");
            }
        }
    }
}
