#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count_character(char * string, char count_me) {
    int myreturn = 0;
    int length, i;
    length = strlen(string);
    for (i=0;i<length;i++) {
        if (string[i] == count_me){
            myreturn++;
        }
    }
    return myreturn;
}

void quick_sort(int * array, int low, int high) {
	int p;
	if (low < high) {
		p = partition(array, low, high);
		quick_sort(array, low, p - 1);
		quick_sort(array, p + 1, high);
	}
}

int partition(int * array, int low, int high) {
	int pivot_index, pivot_value, store_index, i;
	pivot_index = choose_pivot(low, high);
	pivot_value = array[pivot_index];
	swap(array, pivot_index, high);
	store_index = low;
	for (i = low;i<high;i++){
		if (array[i] < pivot_value) {
			swap(array, i, store_index);
			store_index++;
		}
	}

	swap(array, store_index, high);

	return store_index;
}

int choose_pivot(int low, int high) {
	int val;
	val = (high + low) / 2;
	return (val);
}

void swap(int * array, int first, int second){
	int temp;
	temp = array[first];
	array[first] = array[second];
	array[second] = temp;
}

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[92000];
    char * temp;
    int length, num_count, i, hold, done;
    int * array = malloc(1 * sizeof(int));
    while (fgets(line, 92000, file)) {
    //	find L
    	num_count = count_character(line, ',') + 1;
    	
    //	size array appropriately
        array = realloc(array, num_count * sizeof(int));

    //	parse out the numbers  
		temp = strtok(line, ",");
        i = 0;
        while(temp != NULL) {
            array[i] = atoi(temp);
            temp = strtok(NULL, ",");
            i++;
        }

        quick_sort(array, 0, num_count);

	//	count the values!
		done = 0;
		hold = array[0];
        for (i=0; i<num_count; i++) {
			done++;
    		if (hold == array[i]) {
				if (done >= (num_count / 2)) {
					break;
				}
    		}
    		else {
    			hold = array[i];
    			done = 0;
    		}
		}

    //	return the right value
		if (done >= (num_count / 2)) {
			printf("%d\n", hold);
		}
		else {
			printf("None\n");	
		}
    }
}