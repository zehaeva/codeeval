#include <stdio.h>
int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    char a[2];
    char b[2];
    char c[3];
    int i, first_mod, second_mod, max_value; 
    while (fgets(line, 1024, file)) {
    //  Do something with the line
        a[0] = line[0];
        a[1] = '\0';
        b[0] = line[2];
        b[1] = '\0';
        c[0] = line[4];
        c[1] = line[5];
        c[2] = '\0';
        printf("%s:: %s: %s: %s\n\n", line, a, b, c);

        first_mod = 3;
        second_mod = 5;
        max_value = 20;

        for (i = 1;i <= max_value;i++) {
            if (i % first_mod == 0) {
                printf("F");
            }
            if (i % second_mod == 0) {
                printf("B");
            }
            if (i % first_mod != 0 && i % second_mod != 0) {
                printf("%i", i);
            }
            printf("\n");
	    }
    }
    return 0;
}
