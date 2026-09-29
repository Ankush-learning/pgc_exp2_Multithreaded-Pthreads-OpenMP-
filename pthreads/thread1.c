/*
 * thread1.c
 * Create one thread using Pthreads.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part A — Step 1
 *
 * Compile:
 *   gcc thread1.c -o thread1 -pthread
 * Run:
 *   ./thread1
 *
 * Expected output:
 *   Hello from the thread!
 *   Main thread finished.
 */

#include <stdio.h>
#include <pthread.h>

void *thread_function(void *arg)
{
    printf("Hello from the thread!\n");
    return NULL;
}

int main()
{
    pthread_t thread;

    pthread_create(&thread, NULL, thread_function, NULL);
    pthread_join(thread, NULL);

    printf("Main thread finished.\n");
    return 0;
}
