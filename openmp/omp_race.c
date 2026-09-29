/*
 * omp_race.c
 * Demonstrate a race condition in OpenMP — multiple threads increment a
 * shared counter without synchronization, producing an incorrect result.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part B — Step 8
 *
 * Compile:
 *   gcc omp_race.c -o omp_race -fopenmp
 * Run:
 *   ./omp_race
 *
 * Expected output (actual counter will be incorrect):
 *   Expected counter = 400000
 *   Actual counter = <some incorrect value>
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
            counter++;
        }
    }

    printf("Expected counter = %d\n", NUM_THREADS * INCREMENTS);
    printf("Actual counter = %d\n", counter);
    return 0;
}
