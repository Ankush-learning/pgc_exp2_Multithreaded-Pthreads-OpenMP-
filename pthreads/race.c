/*
 * race.c
 * Demonstrate a race condition — multiple threads modify a shared counter
 * without synchronization, producing an incorrect result.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part A — Step 4
 *
 * Compile:
 *   gcc race.c -o race -pthread
 * Run:
 *   ./race
 *
 * Expected output (actual counter will vary each run):
 *   Expected counter = 400000
 *   Actual counter = <some incorrect value>
 */

#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
#define INCREMENTS  100000

int counter = 0;

void *increment_counter(void *arg)
{
    for (int i = 0; i < INCREMENTS; i++) {
        counter++;
    }
    return NULL;
}

int main()
{
    pthread_t threads[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL, increment_counter, NULL);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Expected counter = %d\n", NUM_THREADS * INCREMENTS);
    printf("Actual counter = %d\n", counter);
    return 0;
}
