# Modules

## Writing modules in Python

::: streampu._ext.sts.Stateless

::: streampu._ext.sfl.Stateful

::: streampu._ext.sfl.Stateful_core

## Writing modules in Julia

Only when pyStreamPU is compiled with Julia, see the guide
[Writing a module in Julia](../guides/julia_module.md).

::: streampu._ext.jl.Stateless_Julia

::: streampu._ext.jl.Stateful_Julia

::: streampu._ext.jl.Module_Julia

::: streampu._ext.jl.Julia

::: streampu.julia

## Built-in modules

Factories of the built-in modules. Each function returns a new module whose class
depends on the data type.

### Sources and sinks

::: streampu._source.source_random
::: streampu._source.source_user
::: streampu._source.source_user_binary
::: streampu._sink.sink_no
::: streampu._sink.sink_user_binary

### Processing and utilities

::: streampu._incrementer.incrementer
::: streampu._initializer.initializer
::: streampu._finalizer.finalizer
::: streampu._relayer.relayer
::: streampu._delayer.delayer

## Probes, reporters and terminals

::: streampu._probe.probe_value

::: streampu._ext.prb.Probe_occurrence

::: streampu._ext.prb.Probe_time

::: streampu._ext.prb.Probe_timestamp

::: streampu._ext.prb.Probe_throughput

::: streampu._ext.prb.Probe_latency

::: streampu._ext.reporter.Reporter_probe

::: streampu._ext.terminal.Terminal_dump

::: streampu._ext.terminal.Terminal_std
