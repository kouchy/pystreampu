import argparse
import csv
import time

from downsampler import Downsampler

import streampu as spu


def main(csv_path: str, cpp: bool = False, min_threads: int = 1, max_threads: int = 16, n_iterations: int = 10000):
    long_data_length = 8192
    downsampling_factor = 4

    short_data_length = long_data_length // downsampling_factor
    dtype = spu.uint8

    initializer = spu.initializer(long_data_length, dtype=dtype)
    dwn = Downsampler(N=long_data_length, F=downsampling_factor, dtype=dtype)
    finalizer = spu.finalizer(short_data_length, dtype=dtype)
    relay = spu.relayer(long_data_length, dtype=dtype)  # no sleep: compare the real costs
    input = initializer()

    if cpp:
        r_input = relay(input)
        output = r_input[::4]

    else:
        output = dwn.downsample(input)

    finalizer(output)

    durations = []
    for n_thread in range(min_threads, max_threads + 1):
        sequence_chain = spu._ext.core._Sequence(input.task, n_thread)

        for lt in sequence_chain.get_tasks_per_threads():
            for t in lt:
                t.stats = True

        start = time.perf_counter()
        sequence_chain.exec_n_times(n_iterations)
        end = time.perf_counter()

        sequence_chain.show_stats()

        durations.append((n_thread, end - start))
        print(f"Threads: {n_thread}, Duration: {end - start:.4f} seconds")
        del sequence_chain

    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["n_threads", "duration_seconds"])
        writer.writerows(durations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", default="durations.csv", help="Output CSV file path")
    parser.add_argument("--min-threads", type=int, default=1, help="Minimum number of threads")
    parser.add_argument("--max-threads", type=int, default=16, help="Maximum number of threads")
    parser.add_argument("--n-iterations", type=int, default=10000, help="Number of iterations")
    parser.add_argument("--cpp", action="store_true", help="Use C++ implementation")

    args = parser.parse_args()
    main(
        args.csv,
        cpp=args.cpp,
        min_threads=args.min_threads,
        max_threads=args.max_threads,
        n_iterations=args.n_iterations,
    )
