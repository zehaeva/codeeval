#include <stdio.h>
#include <string.h>
int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024]; 
    char temp[2];
    int length;
    while (fgets(line, 1024, file)) {
    //  Do something with the line
        length = strlen(line);
        for (int i=0;i<length;i++) {
            if (line[i] >= 65 && line[i] <= 90) {
                temp[0] = line[i] + 32;
            }
            else {
                temp[0] = line[i];
            }
            temp[1] = '\0';
            printf("%s", temp);
        }
        //printf("\n");
    }
    return 0;
}
