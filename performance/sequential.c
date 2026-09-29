/*
 * sequential.c
 * Sequential baseline — sum of i*0.000001 for i = 0..N-1 using one thread.
 * Used as the reference time for speedup and efficiency calculations.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part C — Step 11
 *
 * Compile:
 *   gcc sequential.c -o sequential
 * Run:
 *   ./sequential
 *
 * Measured baseline: 1.787650 seconds
 * Result: 499999999500.00
 */

#include <stdio.h>
#include <time.h>

#define N 1000000000L

double get_time()
{
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
}

int main()
{
    double sum = 0.0;

    double start = get_time();

    for (long i = 0; i < N; i++) {
        sum += (double)i * 0.000001;
    }

    double end = get_time();

    printf("Result = %.2f\n", sum);
    printf("Execution time = %.6f seconds\n", end - start);
    return 0;
}
