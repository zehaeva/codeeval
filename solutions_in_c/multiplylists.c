#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int count_spaces(char * string) {
    int myreturn = 0;
    int length, i;
    length = strlen(string);
    for (i=0;i<length;i++) {
        if (isspace(string[i])){
            myreturn++;
        }
    }
    return myreturn;
}

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024]; 
    char * left, * right, * temp;
    int i, length;
    int * left_array = malloc(1 * sizeof(int));
    int * right_array = malloc(1 * sizeof(int));
    while (fgets(line, 1024, file)) {
    //  Do something with the line
        length = strlen(line);
        line[length - 1] = '\0';
        left = strtok(line, "|");
        right = strtok(NULL, "|");

        length = count_spaces(left);

        left_array = realloc(left_array, length * sizeof(int));
        right_array = realloc(right_array, length * sizeof(int));

        temp = strtok(left, " ");
        i = 0;
        while(temp != NULL) {
            left_array[i] = atoi(temp);
            temp = strtok(NULL, " ");
            i++;
        }

        temp = strtok(right, " ");
        i = 0;
        while(temp != NULL) {
            right_array[i] = atoi(temp);
            temp = strtok(NULL, " ");
            i++;
        }

        for (i=0;i<length;i++){
            printf("%d ", left_array[i] * right_array[i]);
        }
        printf("\n");
    }
    return 0;
}