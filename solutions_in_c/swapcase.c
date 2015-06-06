#include <stdio.h>
int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    int length;
    while (fgets(line, 1024, file)) {
        length = strlen(line);
        for (int i = 0;i<length;i++) {
            if (line[i] >= 65 && line[i] <= 90 ) {
                line[i] = line[i] + 32;
            }
            else {
                if (line[i] >= 97 && line[i] <= 122 ){
                    line[i] = line[i] - 32;
                }
            }
        }
        printf("%s\n", line);
    }
    return 0;
} 
