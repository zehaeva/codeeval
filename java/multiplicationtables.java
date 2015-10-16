
import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        for (int i=1;i<=12;i++){
            for (int j=1;j<=12;j++){
                System.out.printf("%4d", (i * j));
            }
            System.out.print("\n");
        }
    }
}
