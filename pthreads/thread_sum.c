/*
 * thread_sum.c
 * Divide work among threads — each thread sums its portion of an array.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part A — Step 3
 *
 * Compile:
 *   gcc thread_sum.c -o thread_sum -pthread
 * Run:
 *   ./thread_sum
 *
 * Expected output (order of thread messages may vary):
 *   Thread 1 calculated sum = 30
 *   Thread 2 calculated sum = 70
 *   Thread 3 calculated sum = 110
 *   Thread 4 calculated sum = 150
 *   Total sum = 360
 */

#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
#define ARRAY_SIZE  8

int array[ARRAY_SIZE] = {10, 20, 30, 40, 50, 60, 70, 80};
int partial_sum[NUM_THREADS];

void *calculate_sum(void *arg)
{
    int thread_id = *(int *)arg;
    int start = thread_id * (ARRAY_SIZE / NUM_THREADS);
    int end   = start    + (ARRAY_SIZE / NUM_THREADS);

    partial_sum[thread_id] = 0;

    for (int i = start; i < end; i++) {
        partial_sum[thread_id] += array[i];
    }

    printf("Thread %d calculated sum = %d\n",
           thread_id + 1, partial_sum[thread_id]);
    return NULL;
}

int main()
{
    pthread_t threads[NUM_THREADS];
    int thread_ids[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++) {
        thread_ids[i] = i;
        pthread_create(&threads[i], NULL, calculate_sum, &thread_ids[i]);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    int total_sum = 0;
    for (int i = 0; i < NUM_THREADS; i++) {
        total_sum += partial_sum[i];
    }

    printf("Total sum = %d\n", total_sum);
    return 0;
}
