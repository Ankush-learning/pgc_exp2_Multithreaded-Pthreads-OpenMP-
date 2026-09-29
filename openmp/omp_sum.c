/*
 * omp_sum.c
 * OpenMP work sharing and reduction — divide array summation across threads.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part B — Step 7
 *
 * Compile:
 *   gcc omp_sum.c -o omp_sum -fopenmp
 * Run:
 *   ./omp_sum
 *
 * Expected output (order may vary):
 *   Thread X processing array[Y] = Z
 *   ...
 *   Total sum = 360
 */

#include <stdio.h>
#include <omp.h>

#define ARRAY_SIZE 8

int array[ARRAY_SIZE] = {10, 20, 30, 40, 50, 60, 70, 80};

int main()
{
    int total_sum = 0;

    #pragma omp parallel for reduction(+:total_sum)
    for (int i = 0; i < ARRAY_SIZE; i++) {
        int thread_id = omp_get_thread_num();
        printf("Thread %d processing array[%d] = %d\n",
               thread_id, i, array[i]);
        total_sum += array[i];
    }

    printf("Total sum = %d\n", total_sum);
    return 0;
}
