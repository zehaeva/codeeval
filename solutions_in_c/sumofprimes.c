#include <stdio.h>
int main(int argc, const char * argv[]) {
    int primes[1000];
    int i, j, k;
    int countofprimes;
    int found;
    int sum;

    primes[0] = 2;
    countofprimes = 1;
    j = 1;
    sum = 2;

    while (countofprimes < 1000) {
        j = j + 2;
        found = 0;
        for (k = 0;k<countofprimes;k++) {
            if (j % primes[k] == 0) {
                found = 1;
                break;
            }
        }
        if (found == 0) {
            primes[countofprimes] = j;
            sum = sum + j;
            countofprimes++;
        }
    }
    printf("%d\n", sum);

    return 0;
}
