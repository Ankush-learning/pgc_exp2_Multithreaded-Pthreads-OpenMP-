import csv
import os
import matplotlib.pyplot as plt

CSV_FILE = "performance/performance_results.csv"
GRAPH_DIR = "performance/graphs"

os.makedirs(GRAPH_DIR, exist_ok=True)

threads = []
pthreads_time = []
openmp_time = []
sequential_time = []

# Read benchmark data
with open(CSV_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        threads.append(int(row["Threads"]))
        pthreads_time.append(float(row["Pthreads_Time_s"]))
        openmp_time.append(float(row["OpenMP_Time_s"]))
        sequential_time.append(float(row["Sequential_Time_s"]))

# Use the first sequential value as the baseline
seq_time = sequential_time[0]

# Calculate speedup
pthreads_speedup = [
    seq_time / t for t in pthreads_time
]

openmp_speedup = [
    seq_time / t for t in openmp_time
]

# Calculate efficiency
pthreads_efficiency = [
    (speedup / thread) * 100
    for speedup, thread in zip(pthreads_speedup, threads)
]

openmp_efficiency = [
    (speedup / thread) * 100
    for speedup, thread in zip(openmp_speedup, threads)
]

# ---------------------------------------------------------
# Graph 1: Execution Time vs Number of Threads
# ---------------------------------------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    threads,
    pthreads_time,
    marker="o",
    linewidth=2,
    label="Pthreads"
)

plt.plot(
    threads,
    openmp_time,
    marker="s",
    linewidth=2,
    label="OpenMP"
)

plt.axhline(
    y=seq_time,
    linestyle="--",
    linewidth=1.5,
    label=f"Sequential ({seq_time:.6f}s)"
)

plt.title("Execution Time vs Number of Threads", fontsize=14, fontweight="bold")
plt.xlabel("Number of Threads", fontsize=12)
plt.ylabel("Execution Time (seconds)", fontsize=12)
plt.xticks(threads)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig(
    f"{GRAPH_DIR}/execution_time.png",
    dpi=300
)

plt.close()

# ---------------------------------------------------------
# Graph 2: Speedup vs Number of Threads
# ---------------------------------------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    threads,
    pthreads_speedup,
    marker="o",
    linewidth=2,
    label="Pthreads"
)

plt.plot(
    threads,
    openmp_speedup,
    marker="s",
    linewidth=2,
    label="OpenMP"
)

# Ideal linear speedup
plt.plot(
    threads,
    threads,
    linestyle="--",
    linewidth=1.5,
    label="Ideal Speedup"
)

plt.title("Speedup vs Number of Threads", fontsize=14, fontweight="bold")
plt.xlabel("Number of Threads", fontsize=12)
plt.ylabel("Speedup (×)", fontsize=12)
plt.xticks(threads)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.ylim(bottom=0)
plt.tight_layout()

plt.savefig(
    f"{GRAPH_DIR}/speedup.png",
    dpi=300
)

plt.close()

# ---------------------------------------------------------
# Graph 3: Efficiency vs Number of Threads
# ---------------------------------------------------------

plt.figure(figsize=(9, 6))

plt.plot(
    threads,
    pthreads_efficiency,
    marker="o",
    linewidth=2,
    label="Pthreads"
)

plt.plot(
    threads,
    openmp_efficiency,
    marker="s",
    linewidth=2,
    label="OpenMP"
)

# Ideal efficiency
plt.axhline(
    y=100,
    linestyle="--",
    linewidth=1.5,
    label="Ideal Efficiency (100%)"
)

plt.title("Efficiency vs Number of Threads", fontsize=14, fontweight="bold")
plt.xlabel("Number of Threads", fontsize=12)
plt.ylabel("Efficiency (%)", fontsize=12)
plt.xticks(threads)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.ylim(0, 115)
plt.tight_layout()

plt.savefig(
    f"{GRAPH_DIR}/efficiency.png",
    dpi=300
)

plt.close()

# ---------------------------------------------------------
# Print calculated results
# ---------------------------------------------------------

print("\nPerformance Analysis")
print("=" * 75)

print(
    f"{'Threads':<10}"
    f"{'Pthreads':<15}"
    f"{'OpenMP':<15}"
    f"{'Pth Speedup':<15}"
    f"{'OMP Speedup':<15}"
)

print("-" * 75)

for i in range(len(threads)):
    print(
        f"{threads[i]:<10}"
        f"{pthreads_time[i]:<15.6f}"
        f"{openmp_time[i]:<15.6f}"
        f"{pthreads_speedup[i]:<15.3f}"
        f"{openmp_speedup[i]:<15.3f}"
    )

print("\n[ DONE ] Graphs generated successfully.")
print(f"Graphs saved in: {GRAPH_DIR}/")
