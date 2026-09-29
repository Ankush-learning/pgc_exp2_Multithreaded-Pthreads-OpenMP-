#!/usr/bin/env python3
"""
generate_graphs.py
Generate performance_results.csv and all three performance graphs
for the Multithreaded Pthreads and OpenMP experiment.

Actual measured values from student's machine.
Sequential baseline: 1.787650 seconds

Usage:
    python3 generate_graphs.py
"""

import csv
import os
import sys

# ---------------------------------------------------------------------------
# Actual measured data (student's machine)
# ---------------------------------------------------------------------------

SEQ_TIME = 1.787650   # seconds

# Official thread counts (3-thread accidental run excluded)
THREADS = [1, 2, 4, 6, 16]

PTHREAD_TIMES = {
    1:  1.789828,
    2:  0.906504,
    4:  0.511658,
    6:  0.357663,
    16: 0.200452,
}

OMP_TIMES = {
    1:  1.785037,
    2:  0.888479,
    4:  0.490306,
    6:  0.359280,
    16: 0.198500,
}

# ---------------------------------------------------------------------------
# Calculations
# ---------------------------------------------------------------------------

def speedup(seq, par):
    return round(seq / par, 4)

def efficiency(spd, n):
    return round((spd / n) * 100, 2)

rows = []
for t in THREADS:
    pt = PTHREAD_TIMES[t]
    ot = OMP_TIMES[t]
    ps = speedup(SEQ_TIME, pt)
    os_ = speedup(SEQ_TIME, ot)
    pe = efficiency(ps, t)
    oe = efficiency(os_, t)
    rows.append({
        "Threads":              t,
        "Pthreads_Time_s":      pt,
        "OpenMP_Time_s":        ot,
        "Pthreads_Speedup":     ps,
        "OpenMP_Speedup":       os_,
        "Pthreads_Efficiency":  pe,
        "OpenMP_Efficiency":    oe,
    })

# ---------------------------------------------------------------------------
# Write CSV
# ---------------------------------------------------------------------------

script_dir  = os.path.dirname(os.path.abspath(__file__))
perf_dir    = script_dir
graphs_dir  = os.path.join(perf_dir, "graphs")
os.makedirs(graphs_dir, exist_ok=True)

csv_path = os.path.join(perf_dir, "performance_results.csv")
fieldnames = [
    "Threads",
    "Pthreads_Time_s", "OpenMP_Time_s",
    "Pthreads_Speedup", "OpenMP_Speedup",
    "Pthreads_Efficiency", "OpenMP_Efficiency",
]

with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"[OK] CSV written: {csv_path}")

# Print table to terminal
print()
print(f"{'Threads':>7} | {'Pth Time':>9} | {'OMP Time':>9} | "
      f"{'Pth Spd':>8} | {'OMP Spd':>8} | {'Pth Eff%':>9} | {'OMP Eff%':>9}")
print("-" * 75)
for r in rows:
    print(f"{r['Threads']:>7} | {r['Pthreads_Time_s']:>9.6f} | "
          f"{r['OpenMP_Time_s']:>9.6f} | "
          f"{r['Pthreads_Speedup']:>8.4f} | {r['OpenMP_Speedup']:>8.4f} | "
          f"{r['Pthreads_Efficiency']:>8.2f}% | {r['OpenMP_Efficiency']:>8.2f}%")

# ---------------------------------------------------------------------------
# Graphs (matplotlib)
# ---------------------------------------------------------------------------

try:
    import matplotlib
    matplotlib.use("Agg")   # non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
except ImportError:
    print("\n[WARN] matplotlib not available — skipping graph generation.")
    print("       Install with:  pip install matplotlib")
    sys.exit(0)

thread_vals  = [r["Threads"]             for r in rows]
pt_times     = [r["Pthreads_Time_s"]     for r in rows]
omp_times    = [r["OpenMP_Time_s"]       for r in rows]
pt_speedup   = [r["Pthreads_Speedup"]    for r in rows]
omp_speedup  = [r["OpenMP_Speedup"]      for r in rows]
pt_eff       = [r["Pthreads_Efficiency"] for r in rows]
omp_eff      = [r["OpenMP_Efficiency"]   for r in rows]

STYLE = {
    "pth_color":  "#2196F3",   # blue
    "omp_color":  "#FF5722",   # deep orange
    "seq_color":  "#9E9E9E",   # grey
    "ideal_color":"#4CAF50",   # green
    "figsize":    (8, 5),
    "dpi":        150,
    "linewidth":  2.2,
    "markersize": 7,
}

def save_fig(fig, filename):
    path = os.path.join(graphs_dir, filename)
    fig.savefig(path, dpi=STYLE["dpi"], bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] Graph saved: {path}")

# ------------------------------------------------------------------
# Graph 1 — Execution Time vs Number of Threads
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=STYLE["figsize"])

ax.axhline(y=SEQ_TIME, color=STYLE["seq_color"], linestyle="--",
           linewidth=1.5, label=f"Sequential baseline ({SEQ_TIME:.6f} s)")

ax.plot(thread_vals, pt_times,
        color=STYLE["pth_color"], marker="o",
        linewidth=STYLE["linewidth"], markersize=STYLE["markersize"],
        label="Pthreads")

ax.plot(thread_vals, omp_times,
        color=STYLE["omp_color"], marker="s",
        linewidth=STYLE["linewidth"], markersize=STYLE["markersize"],
        label="OpenMP")

ax.set_title("Execution Time vs Number of Threads", fontsize=14, fontweight="bold")
ax.set_xlabel("Number of Threads", fontsize=12)
ax.set_ylabel("Execution Time (seconds)", fontsize=12)
ax.set_xticks(thread_vals)
ax.legend(fontsize=10)
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_ylim(bottom=0)

save_fig(fig, "execution_time.png")

# ------------------------------------------------------------------
# Graph 2 — Speedup vs Number of Threads
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=STYLE["figsize"])

ideal_speedup = thread_vals  # 1x, 2x, 4x, 6x, 16x
ax.plot(thread_vals, ideal_speedup,
        color=STYLE["ideal_color"], linestyle="--",
        linewidth=1.5, label="Ideal (linear) speedup")

ax.plot(thread_vals, pt_speedup,
        color=STYLE["pth_color"], marker="o",
        linewidth=STYLE["linewidth"], markersize=STYLE["markersize"],
        label="Pthreads")

ax.plot(thread_vals, omp_speedup,
        color=STYLE["omp_color"], marker="s",
        linewidth=STYLE["linewidth"], markersize=STYLE["markersize"],
        label="OpenMP")

ax.set_title("Speedup vs Number of Threads", fontsize=14, fontweight="bold")
ax.set_xlabel("Number of Threads", fontsize=12)
ax.set_ylabel("Speedup", fontsize=12)
ax.set_xticks(thread_vals)
ax.legend(fontsize=10)
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_ylim(bottom=0)

save_fig(fig, "speedup.png")

# ------------------------------------------------------------------
# Graph 3 — Efficiency vs Number of Threads
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=STYLE["figsize"])

ax.axhline(y=100, color=STYLE["ideal_color"], linestyle="--",
           linewidth=1.5, label="Ideal efficiency (100%)")

ax.plot(thread_vals, pt_eff,
        color=STYLE["pth_color"], marker="o",
        linewidth=STYLE["linewidth"], markersize=STYLE["markersize"],
        label="Pthreads")

ax.plot(thread_vals, omp_eff,
        color=STYLE["omp_color"], marker="s",
        linewidth=STYLE["linewidth"], markersize=STYLE["markersize"],
        label="OpenMP")

ax.set_title("Efficiency vs Number of Threads", fontsize=14, fontweight="bold")
ax.set_xlabel("Number of Threads", fontsize=12)
ax.set_ylabel("Efficiency (%)", fontsize=12)
ax.set_xticks(thread_vals)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f%%"))
ax.legend(fontsize=10)
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_ylim(0, 115)

save_fig(fig, "efficiency.png")

print("\n[DONE] All outputs generated successfully.")
