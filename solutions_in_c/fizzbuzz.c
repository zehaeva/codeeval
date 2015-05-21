#include <stdio.h>
int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    char* parse;
    int first_mod, second_mod, max_value, i; 
    while (fgets(line, 1024, file)) {
    //  Do something with the line

        sscanf(line, "%d %d %d", &first_mod, &second_mod, &max_value);

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
            printf(" ");
	    }
        printf("\n");    
    }
    return 0;
}
