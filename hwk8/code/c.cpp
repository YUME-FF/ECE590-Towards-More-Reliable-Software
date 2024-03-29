#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define N_THREADS 100

int counter;

void * thread_code(void * arg) {
  counter += 1;
  pthread_exit(0);
}

void start_threads() {
  int i;
  pthread_t threads[N_THREADS];
  counter = 0;  // Reset counter to 0 before starting threads

  for (i = 0; i < N_THREADS; i++) {
    pthread_create(&threads[i], NULL, thread_code, NULL);
  }

  for (i = 0; i < N_THREADS; i++) {
    pthread_join(threads[i], NULL);
  }
}

void test(int nums) {
  int pass = 0;
  for (int i = 0; i < nums; i++) {
    start_threads();
    if (counter == N_THREADS) {
      pass++;
    }
  }
  double passRate = ((double)pass / nums) * 100;
  printf("For %d executions: Passed %d tests. Pass rate: %.2f%%\n", nums, pass, passRate);
}

int main() {
  int testCounts[] = {10, 100, 1000, 3000, 8000, 10000, 15000};
  int numberOfTests = sizeof(testCounts) / sizeof(testCounts[0]);

  for (int i = 0; i < numberOfTests; i++) {
    test(testCounts[i]);
  }

  return EXIT_SUCCESS;
}
