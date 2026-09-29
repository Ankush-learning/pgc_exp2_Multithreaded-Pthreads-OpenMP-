/*
 * omp_perf.c
 * Measure OpenMP parallel performance — sum of i*0.000001 for i = 0..N-1.
 * OpenMP distributes the loop automatically across the specified threads.
 *
 * Experiment: Multithreaded Programming Using Pthreads and OpenMP
 * Part C — Step 14
 *
 * Compile:
 *   gcc omp_perf.c -o omp_perf -fopenmp
 * Run:
 *   ./omp_perf
 *   Enter number of threads: <1, 2, 4, 6, or 16>
 *
 * Expected output:
 *   Result = 499999999500.00
 *   Execution time = X.XXXXXX seconds
 */

#include <stdio.h>
#include <omp.h>
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
    int num_threads;

    printf("Enter number of threads: ");
    scanf(" %d", &num_threads);

    if (num_threads < 1 || num_threads > 32) {
        printf("Please enter a value between 1 and 32.\n");
        return 1;
    }

    omp_set_num_threads(num_threads);

    double start_time = get_time();

    #pragma omp parallel for reduction(+:sum)
    for (long i = 0; i < N; i++) {
        sum += (double)i * 0.000001;
    }

    double end_time = get_time();

    printf("Result = %.2f\n", sum);
    printf("Execution time = %.6f seconds\n", end_time - start_time);
    return 0;
}
