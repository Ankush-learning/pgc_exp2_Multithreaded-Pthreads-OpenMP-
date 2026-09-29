/*
 * omp_barrier.c
 * Demonstrate OpenMP barrier — all threads complete Stage 1 before
 * any thread starts Stage 2.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part B — Step 10
 *
 * Compile:
 *   gcc omp_barrier.c -o omp_barrier -fopenmp
 * Run:
 *   ./omp_barrier
 *
 * Expected pattern:
 *   All "completed Stage 1" messages appear before any "started Stage 2"
 */

#include <stdio.h>
#include <omp.h>

int main()
{
    omp_set_num_threads(4);

    #pragma omp parallel
    {
        int thread_id = omp_get_thread_num();

        printf("Thread %d completed Stage 1\n", thread_id);

        #pragma omp barrier

        printf("Thread %d started Stage 2\n", thread_id);
    }
    return 0;
}
