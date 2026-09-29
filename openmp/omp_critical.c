/*
 * omp_critical.c
 * Fix the OpenMP race condition using a critical section.
 * Only one thread at a time enters the protected block.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part B — Step 9
 *
 * Compile:
 *   gcc omp_critical.c -o omp_critical -fopenmp
 * Run:
 *   ./omp_critical
 *
 * Expected output:
 *   Expected counter = 400000
 *   Actual counter = 400000
 */

#include <stdio.h>
#include <omp.h>

#define NUM_THREADS 4
#define INCREMENTS  100000

int counter = 0;

int main()
{
    omp_set_num_threads(NUM_THREADS);

    #pragma omp parallel
    {
        for (int i = 0; i < INCREMENTS; i++) {
            #pragma omp critical
            {
                counter++;
            }
        }
    }

    printf("Expected counter = %d\n", NUM_THREADS * INCREMENTS);
    printf("Actual counter = %d\n", counter);
    return 0;
}
