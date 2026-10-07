# Multithreaded Programming Using Pthreads and OpenMP

## Parallel and Graph Computing – Experiment 2

This project demonstrates multithreaded programming and parallel computing concepts using **POSIX Threads (Pthreads)** and **OpenMP**.

The experiment covers thread creation, work distribution, race conditions, synchronization, barrier coordination, reduction operations, and performance analysis.

---

## Team Members

| Name | USN |
|---|---|
| Ankush | 01FE24BCI096 |
| Shrikar | 01FE24BCI013 |
| Shreya | 01FE24BCI033 |
| Sai Shree Ram | 01FE24BCI034 |

**University:** KLE Technological University, Hubballi
**Program:** Computer Science and Artificial Intelligence

---

## 1. Objectives

The objectives of this experiment are:

1. Understand the fundamentals of multithreaded and parallel programming.
2. Create and manage threads using Pthreads.
3. Implement parallel programs using OpenMP.
4. Understand work distribution and domain decomposition.
5. Demonstrate race conditions in shared-memory programs.
6. Apply synchronization using Pthread mutexes.
7. Apply synchronization using OpenMP critical sections.
8. Understand barrier synchronization.
9. Demonstrate reduction operations in OpenMP.
10. Benchmark sequential, Pthreads, and OpenMP implementations.
11. Calculate speedup for different thread counts.
12. Calculate parallel efficiency and analyze scalability.

---

## 2. Technologies Used

- **Programming Language:** C
- **Python:** Graph generation and performance analysis
- **Compiler:** GCC
- **Operating System:** Ubuntu Linux through WSL
- **Pthreads:** POSIX Threads
- **OpenMP:** Open Multi-Processing
- **Version Control:** Git and GitHub

### Compilation Flags

Pthreads programs:

```bash
gcc filename.c -o filename -pthread
```

OpenMP programs:

```bash
gcc filename.c -o filename -fopenmp
```

Sequential program:

```bash
gcc sequential.c -o sequential
```

---

## 3. Project Structure

```text
pgc_exp2_Multithreaded-Pthreads-OpenMP/
│
├── README.md
├── .gitignore
│
├── pthreads/
│   ├── thread1.c
│   ├── thread2.c
│   ├── thread_sum.c
│   ├── race.c
│   ├── mutex.c
│   └── pthread_perf.c
│
├── openmp/
│   ├── omp1.c
│   ├── omp_sum.c
│   ├── omp_race.c
│   ├── omp_critical.c
│   ├── omp_barrier.c
│   └── omp_perf.c
│
├── performance/
│   ├── sequential.c
│   ├── generate_graphs.py
│   ├── performance_results.csv
│   └── graphs/
│       ├── execution_time.png
│       ├── speedup.png
│       └── efficiency.png
│
```

---

# 4. Pthreads Experiments

## Step 1 – Single Thread

**File:** `pthreads/thread1.c`

A single worker thread is created using `pthread_create()`.

The main thread waits for the worker thread using `pthread_join()`.

### Concepts

- `pthread_create()`
- `pthread_join()`
- Thread lifecycle
- Worker thread execution

---

## Step 2 – Multiple Threads

**File:** `pthreads/thread2.c`

Four threads are created simultaneously.

The program demonstrates that threads may execute in a different order depending on operating system scheduling.

### Concepts

- Multiple concurrent threads
- Thread IDs
- Argument passing
- Non-deterministic scheduling

Example output:

```text
Hello from Thread 1
Hello from Thread 3
Hello from Thread 4
Hello from Thread 2
All threads have finished.
```

The order may change between executions.

---

## Step 3 – Work Distribution

**File:** `pthreads/thread_sum.c`

An array is divided among four threads.

Each thread calculates a partial sum and the partial results are combined to produce the final sum.

### Result

```text
Thread 1 calculated sum = 30
Thread 2 calculated sum = 70
Thread 3 calculated sum = 110
Thread 4 calculated sum = 150
Total sum = 360
```

### Concepts

- Domain decomposition
- Work distribution
- Partial results
- Thread-based computation

---

## Step 4 – Race Condition

**File:** `pthreads/race.c`

Four threads increment a shared counter 100,000 times each.

The expected result is:

```text
400000
```

However, the program does not use synchronization.

### Observed Result

```text
Expected counter = 400000
Actual counter = 105873
```

The actual value is smaller because multiple threads can read and modify the shared variable simultaneously, causing **lost updates**.

### Concept

A race condition occurs when multiple threads access shared data concurrently and the final result depends on the timing of their execution.

---

## Step 5 – Mutex Synchronization

**File:** `pthreads/mutex.c`

The race condition is fixed using a Pthread mutex.

The critical section is protected using:

```c
pthread_mutex_lock()
pthread_mutex_unlock()
```

### Result

```text
Expected counter = 400000
Actual counter = 400000
```

The mutex ensures that only one thread modifies the shared counter at a time.

---

## Step 6 – Pthreads Performance

**File:** `pthreads/pthread_perf.c`

A large numerical computation is performed using different numbers of threads.

The benchmark uses:

```text
N = 1,000,000,000 iterations
```

The computation calculates:

```text
sum(i × 10^-6)
```

for:

```text
i = 0 ... N-1
```

The verified result is:

```text
499999999500.00
```

Thread counts tested:

```text
1, 2, 4, 6, 16
```

---

# 5. OpenMP Experiments

## Step 7 – Basic Parallel Region

**File:** `openmp/omp1.c`

OpenMP is used to create a parallel region.

The program displays:

- Thread ID
- Total number of threads

Example:

```text
Hello from Thread 0 of 12
Hello from Thread 1 of 12
...
```

The execution order of threads is not guaranteed.

### Concepts

```c
#pragma omp parallel
omp_get_thread_num()
omp_get_num_threads()
```

---

## Step 8 – Work Sharing and Reduction

**File:** `openmp/omp_sum.c`

The array is processed using OpenMP parallel work sharing.

A reduction operation is used to safely combine partial results.

### Result

```text
Total sum = 360
```

### Important Directive

```c
#pragma omp parallel for reduction(+:total_sum)
```

Reduction avoids the race condition that would occur if all threads directly modified the same variable.

---

## Step 9 – OpenMP Race Condition

**File:** `openmp/omp_race.c`

Four OpenMP threads increment a shared counter without synchronization.

### Observed Result

```text
Expected counter = 400000
Actual counter = 100188
```

The result is incorrect because the shared variable is accessed concurrently without protection.

---

## Step 10 – OpenMP Critical Section

**File:** `openmp/omp_critical.c`

The race condition is fixed using:

```c
#pragma omp critical
```

### Result

```text
Expected counter = 400000
Actual counter = 400000
```

The critical section ensures that only one thread executes the protected section at a time.

---

## Step 11 – Barrier Synchronization

**File:** `openmp/omp_barrier.c`

The program contains two execution stages.

All threads must finish Stage 1 before any thread can begin Stage 2.

This is achieved using:

```c
#pragma omp barrier
```

Example output:

```text
Thread 3 completed Stage 1
Thread 0 completed Stage 1
Thread 1 completed Stage 1
Thread 2 completed Stage 1

Thread 2 started Stage 2
Thread 3 started Stage 2
Thread 0 started Stage 2
Thread 1 started Stage 2
```

### Concept

A barrier provides synchronization between phases of parallel execution.

---

## Step 12 – OpenMP Performance

**File:** `openmp/omp_perf.c`

The same numerical workload used for the Pthreads benchmark is implemented using OpenMP.

The following thread counts were tested:

```text
1, 2, 4, 6, 16
```

The verified computation result was:

```text
499999999500.00
```

---

# 6. Performance Analysis

The performance experiment compares:

- Sequential execution
- Pthreads
- OpenMP

### Workload

```text
N = 1,000,000,000 iterations
```

### Verified Result

```text
499999999500.00
```

### Sequential Baseline

The measured sequential execution time was:

```text
3.547489 seconds
```

---

## 6.1 Execution Time Results

The following measurements were obtained on the test system.

| Threads | Pthreads Time (s) | OpenMP Time (s) |
|---:|---:|---:|
| 1 | 3.318546 | 3.373385 |
| 2 | 1.895705 | 1.387085 |
| 4 | 0.725044 | 0.716352 |
| 6 | 0.591749 | 0.568732 |
| 16 | 0.417068 | 0.399610 |

### Observation

Execution time decreases as the number of threads increases.

OpenMP produced a lower execution time than Pthreads at 2, 4, 6, and 16 threads in this experiment.

---

# 7. Speedup

Speedup is calculated using:

```text
Speedup = Sequential Execution Time / Parallel Execution Time
```

The sequential baseline was:

```text
3.547489 seconds
```

### Speedup Results

| Threads | Pthreads Speedup | OpenMP Speedup |
|---:|---:|---:|
| 1 | 1.069× | 1.052× |
| 2 | 1.871× | 2.558× |
| 4 | 4.893× | 4.952× |
| 6 | 5.995× | 6.238× |
| 16 | 8.506× | 8.877× |

### Observation

At 16 threads:

- Pthreads achieved **8.506× speedup**
- OpenMP achieved **8.877× speedup**

OpenMP achieved the highest speedup in this experiment.

---

# 8. Parallel Efficiency

Parallel efficiency is calculated using:

```text
Efficiency (%) = (Speedup / Number of Threads) × 100
```

### Efficiency Results

| Threads | Pthreads Efficiency | OpenMP Efficiency |
|---:|---:|---:|
| 1 | 106.90% | 105.16% |
| 2 | 93.57% | 127.88% |
| 4 | 122.32% | 123.80% |
| 6 | 99.92% | 103.96% |
| 16 | 53.16% | 55.48% |

### Note on Efficiency Above 100%

Some calculated efficiency values are above 100%.

This does not mean the parallel implementation achieved physically impossible performance.

The sequential and parallel programs were measured in separate executions. Small differences in CPU frequency, operating-system scheduling, cache state, and system load can cause timing variation.

Therefore, values slightly above 100% should be interpreted as measurement variation around the ideal value rather than literal superlinear efficiency.

---

# 9. Graphs

## Execution Time vs Number of Threads

This graph compares the execution time of Pthreads and OpenMP as the number of threads increases.

![Execution Time](performance/graphs/execution_time.png)

---

## Speedup vs Number of Threads

This graph compares the measured speedup with the ideal linear speedup.

![Speedup](performance/graphs/speedup.png)

---

## Efficiency vs Number of Threads

This graph shows the parallel efficiency of Pthreads and OpenMP.

![Efficiency](performance/graphs/efficiency.png)

---

# 10. Comparison: Pthreads vs OpenMP

| Feature | Pthreads | OpenMP |
|---|---|---|
| Thread creation | Explicit | Mostly automatic |
| Thread management | Programmer controlled | Runtime managed |
| Work distribution | Manual | Compiler/runtime assisted |
| Synchronization | Mutexes, joins, etc. | Critical, barrier, reduction, etc. |
| Programming complexity | Higher | Lower |
| Control | Fine-grained | Higher-level abstraction |
| Performance in this experiment | Very good | Slightly better overall |

### Key Observation

Both Pthreads and OpenMP provide significant performance improvements over the sequential implementation.

OpenMP achieved slightly better performance for the tested workload at higher thread counts while requiring less explicit thread-management code.

---

# 11. Key Concepts Demonstrated

### Thread Creation

Pthreads:

```c
pthread_create()
```

OpenMP:

```c
#pragma omp parallel
```

### Thread Synchronization

Pthreads:

```c
pthread_mutex_lock()
pthread_mutex_unlock()
```

OpenMP:

```c
#pragma omp critical
```

### Barrier Synchronization

```c
#pragma omp barrier
```

### Reduction

```c
#pragma omp parallel for reduction(+:sum)
```

### Thread Joining

```c
pthread_join()
```

---

# 12. How to Run the Experiments

## Pthreads

Example:

```bash
gcc pthreads/thread1.c -o thread1 -pthread
./thread1
```

For the performance benchmark:

```bash
gcc pthreads/pthread_perf.c -o pthread_perf -pthread
./pthread_perf
```

Enter one of:

```text
1
2
4
6
16
```

---

## OpenMP

Example:

```bash
gcc openmp/omp1.c -o omp1 -fopenmp
./omp1
```

For the performance benchmark:

```bash
gcc openmp/omp_perf.c -o omp_perf -fopenmp
./omp_perf
```

Enter one of:

```text
1
2
4
6
16
```

---

## Sequential

```bash
gcc performance/sequential.c -o sequential
./sequential
```

---

# 13. Generating Performance Graphs

The graph-generation script is written in Python.

Run:

```bash
python performance/generate_graphs.py
```

The generated graphs are stored in:

```text
performance/graphs/
```

The script generates:

```text
execution_time.png
speedup.png
efficiency.png
```

---

# 14. Conclusion

This experiment demonstrates the fundamental concepts of multithreaded and parallel programming using both **Pthreads** and **OpenMP**.

The Pthreads experiments demonstrated explicit thread creation, multiple concurrent threads, work distribution, race conditions, and mutex-based synchronization.

The OpenMP experiments demonstrated parallel regions, work sharing, reduction, race conditions, critical sections, and barrier synchronization.

The performance analysis showed that both approaches can significantly reduce execution time compared with sequential execution.

For the tested workload, the best measured results were obtained using **16 threads**:

```text
Pthreads = 0.417068 seconds
OpenMP   = 0.399610 seconds
```

The corresponding speedups were:

```text
Pthreads = 8.506×
OpenMP   = 8.877×
```

Thus, OpenMP achieved a slightly better performance than Pthreads for the tested workload.

The experiment also demonstrates that increasing the number of threads does not result in unlimited performance improvement. At higher thread counts, factors such as thread-management overhead, scheduling, hardware resources, and contention reduce parallel efficiency.

Overall, the experiment provides practical understanding of **thread concurrency, synchronization, race conditions, parallel workload distribution, speedup, efficiency, and scalability**.

---

## Author

**KLE Technological University – Computer Science and Artificial Intelligence**

Parallel and Graph Computing – Experiment 2
