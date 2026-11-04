"""Tests for probes."""

import pathlib

import streampu as spu


def test_probe_report_generation(tmp_path):
    speed = spu.array([1.0], dtype=spu.float32)
    distance = spu.array([1000.0], dtype=spu.float32)
    duration = distance / speed

    reporter = spu.Reporter_probe("Experiment title", "Subtitle")
    prb_occurrence = spu.Probe_occurrence("Line no", reporter)

    prb_speed = spu.probe_value(1, "Speed", reporter, spu.float32)
    prb_speed.set_col_unit("(m/s)")
    prb_speed.set_col_fmtflags(spu.FormatFlags.fixed | spu.FormatFlags.showpoint)
    prb_speed.set_col_prec(0)

    prb_distance = spu.probe_value(1, "Distance", reporter, spu.float32)
    prb_distance.set_col_unit("(m)")
    prb_distance.set_col_fmtflags(spu.FormatFlags.fixed)
    prb_distance.set_col_prec(0)

    prb_duration = spu.probe_value(1, "Duration", reporter, spu.float32)
    prb_duration.set_col_unit("(s)")
    prb_duration.set_col_prec(2)

    prb_time = spu.Probe_time("Sim. time", reporter)
    prb_time.set_col_unit("(s)")

    prb_occurrence()
    prb_occurrence.probe.bind(speed)
    prb_speed(speed)
    prb_distance(distance)

    prb_duration(duration)
    prb_time()
    prb_time.probe.bind(speed)
    speed *= 4

    terminal = spu.Terminal_dump([reporter])
    seq = spu.Sequence([speed, distance, duration])
    spu.rang.disable_colors()

    path = tmp_path / "probe_report.txt"
    with open(path, "w") as f:
        terminal.legend(stream=f)
        seq.exec_n_times(4, terminal, stream=f)
        terminal.report(stream=f)

    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line, end="")
        content = "".join(lines)

    assert len(lines) == 13
    assert "Experiment title" in content
    assert "Speed" in content
    assert "Distance" in content
    assert "Duration" in content
    assert "Sim. time" in content


if __name__ == "__main__":
    cwd = pathlib.Path.cwd()
    test_probe_report_generation(cwd)
