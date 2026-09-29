/*
 * omp1.c
 * OpenMP basic parallel region — identify each thread and the total count.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part B — Step 6
 *
 * Compile:
 *   gcc omp1.c -o omp1 -fopenmp
 * Run:
 *   ./omp1
 *
 * Expected output (order will vary):
 *   Hello from Thread 0 of N
 *   Hello from Thread 1 of N
 *   ...
 */

#include <stdio.h>
#include <omp.h>

int main()
{
    #pragma omp parallel
    {
        int thread_id    = omp_get_thread_num();
        int total_threads = omp_get_num_threads();
        printf("Hello from Thread %d of %d\n", thread_id, total_threads);
    }
    return 0;
}
