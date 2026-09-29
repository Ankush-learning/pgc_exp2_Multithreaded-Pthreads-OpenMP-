/*
 * thread2.c
 * Create multiple threads using Pthreads.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part A — Step 2
 *
 * Compile:
 *   gcc thread2.c -o thread2 -pthread
 * Run:
 *   ./thread2
 *
 * Expected output (order may vary):
 *   Hello from Thread 1
 *   Hello from Thread 2
 *   Hello from Thread 3
 *   Hello from Thread 4
 *   All threads have finished.
 */

#include <stdio.h>
#include <pthread.h>

void *thread_function(void *arg)
{
    int thread_id = *(int *)arg;
    printf("Hello from Thread %d\n", thread_id);
    return NULL;
}

int main()
{
    pthread_t threads[4];
    int thread_ids[4];

    for (int i = 0; i < 4; i++) {
        thread_ids[i] = i + 1;
        pthread_create(&threads[i], NULL, thread_function, &thread_ids[i]);
    }

    for (int i = 0; i < 4; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("All threads have finished.\n");
    return 0;
}
