#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void print_primes(int * pool) {
  int num_of_primes = sizeof(pool);
  int i;
  printf("Number of Primes: %d", num_of_primes);
  for (i=0;i<num_of_primes;i++) {
    printf("%d", pool[i]);
    if (i < num_of_primes - 1) {
      printf(", ");
    }
  }
  printf("\n");
}

void clean_pool(int * pool, int max_value) {
  int i, j, x, y;
  int new_prime = pool[0];
  if (new_prime * new_prime < max_value) {
    int last_index = 0;
    int pool_length = sizeof(pool);
    int delete[pool_length];
    for(i=0;i<pool_length;i++) {
      delete[i] = 0;
    }
    delete[0] = 1;
    for (i=0;i<pool_length;i++) {
      x = pool[i];
      y = x * new_prime;
      if (y < max_value) {
        for (j=last_index;j<pool_length;j++) {
          if (y == pool[j]) {
            delete[j] = 1;
            last_index = j;
            break;
          }
        }
      }
      else {
        break;
      }
    }

    int drained_length = 0;
    for (i=0;i<pool_length;i++) {
      if (delete[i] == 0) {
        drained_length++;
      }
    }
    int drain_pool[drained_length];
    int d_index = 0;
    for (i=0;i<pool_length;i++) {
      if (delete[i] == 0) {
        drain_pool[d_index] = pool[i];
        d_index++;
      }
    }
    clean_pool(drain_pool, max_value);
    pool = realloc(pool, sizeof(int) * sizeof(drain_pool) + sizeof(int));
    pool[0] = new_prime;
    for (i=1;i<sizeof(pool);i++) {
      pool[i] = drain_pool[i - 1];
    }
  }
}
int main(void) {
  int min = 3;
  int max = 100;
  int i, j;
  int * primes = malloc(1 * sizeof(int));
  int num_of_primes = 1;
  int is_this_prime;
  primes[0] = 2;
  for (i=min;i<=max;i=i+2) {
    is_this_prime = 0;
    for (j=0;j<num_of_primes;j++) {
      if (i % primes[j] == 0) {
        is_this_prime = 1;
        break;
      }
    }
    if (is_this_prime == 0) {
      num_of_primes++;
      primes = realloc(primes, num_of_primes * sizeof(int));
      primes[num_of_primes - 1] = i;
    }
  }
  /*
  for (i=0;i<num_of_primes;i++) {
    printf("%d", primes[i]);
    if (i < num_of_primes - 1) {
      printf(", ");
    }
  }*/
  printf("\n");
  print_primes(primes);

  int pool[max];
  for (i=0;i<=max;i++) {
    pool[i] = i;
  }

  clean_pool(pool, max);
  num_of_primes = sizeof(pool);
  for (i=0;i<num_of_primes;i++) {
    printf("%d", pool[i]);
    if (i < num_of_primes - 1) {
      printf(", ");
    }
  }
  printf("\n");

  return 0;
}
