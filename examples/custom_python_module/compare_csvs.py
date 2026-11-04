"""Plot the durations measured by custom_python_module.py for several configurations.

Usage:
    python compare_csvs.py a.csv b.csv --labels "Config A" "Config B" --log --output comparison.png
"""

import argparse
import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # write the file without opening a window

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

# Categorical palette, in fixed order (one color per configuration)
COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*"]
INK, MUTED, GRID = "#1f1f1e", "#6b6a64", "#e4e3de"


def read_duration_csv(csv_path: Path):
    threads = []
    durations = []
    with csv_path.open(newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            threads.append(int(row["n_threads"]))
            durations.append(float(row["duration_seconds"]))
    return threads, durations


def _spread(values, min_gap):
    """Move the y positions of the direct labels apart so that they do not overlap."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    out = list(values)
    for prev, cur in zip(order, order[1:]):
        out[cur] = max(out[cur], out[prev] + min_gap)
    return out


def plot_csv_files(csv_files, labels, output_path: Path, title: str, log: bool = False):
    fig, ax = plt.subplots(figsize=(8, 4.6))
    series = [read_duration_csv(Path(f)) for f in csv_files]

    ends = []
    for i, ((threads, durations), label) in enumerate(zip(series, labels)):
        color = COLORS[i % len(COLORS)]
        ax.plot(
            threads,
            durations,
            color=color,
            linewidth=2,
            marker=MARKERS[i % len(MARKERS)],
            markersize=5,
            markeredgecolor="white",
            markeredgewidth=1,
            label=label,
            zorder=3,
        )
        ends.append((threads[-1], durations[-1]))

    # Direct labels at the end of the lines (text in ink, the marker beside it carries the color)
    if log:
        # Spread the labels in log space, so that the gap looks the same at every height
        label_y = [10**y for y in _spread([math.log10(y) for _, y in ends], min_gap=0.12)]
    else:
        y_max = max(max(d) for _, d in series)
        label_y = _spread([y for _, y in ends], min_gap=0.055 * y_max)
    for (x, _), y, label in zip(ends, label_y, labels):
        ax.annotate(label, xy=(x, y), xytext=(8, 0), textcoords="offset points", va="center", fontsize=8.5, color=INK)

    ax.set_title(title, loc="left", fontsize=11, color=INK)
    ax.set_xlabel("Number of threads", color=MUTED)
    ax.set_ylabel("Duration (s, log scale)" if log else "Duration (s)", color=MUTED)
    if log:
        ax.set_yscale("log")
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
    else:
        ax.set_ylim(bottom=0)
    ax.set_xticks(series[0][0][1::2] if len(series[0][0]) > 8 else series[0][0])
    ax.grid(True, axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, frameon=False, fontsize=9, labelcolor=INK)
    fig.tight_layout()
    fig.subplots_adjust(right=0.80)
    fig.savefig(output_path, dpi=150)
    print(f"written to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Plot multiple duration CSV files on the same graph.")
    parser.add_argument("csv_files", nargs="+", help="Input CSV files")
    parser.add_argument("--labels", nargs="+", help="One label per CSV file (default: the file names)")
    parser.add_argument("--title", default="Duration vs. number of threads", help="Title of the graph")
    parser.add_argument("--log", action="store_true", help="Logarithmic scale for the durations")
    parser.add_argument("--output", default="comparison.png", help="Output image file")
    args = parser.parse_args()

    labels = args.labels or [Path(f).stem for f in args.csv_files]
    if len(labels) != len(args.csv_files):
        parser.error("--labels needs one label per CSV file")
    plot_csv_files(args.csv_files, labels, Path(args.output), args.title, args.log)


if __name__ == "__main__":
    main()
