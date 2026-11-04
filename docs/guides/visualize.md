# Visualizing a graph

When a graph grows, it becomes hard to check from the code how its tasks are bound. A
sequence (or a pipeline) can export its graph in the
[Graphviz](https://graphviz.org/) DOT format.

## Export the graph

```python
import streampu as spu

src = spu.source_random(8, dtype=spu.int64)
inc = spu.incrementer(8, dtype=spu.int64)
out_data, _ = src.generate()
out = inc.increment(out_data)

seq = spu.Sequence(out)
seq.export_dot("seq.dot")
```

`spu.Pipeline` provides the same `export_dot` method.

## Render it

With Graphviz installed, convert the file into an image:

```bash
dot -Tsvg seq.dot -o seq.svg
```

or from Python, with the [`graphviz`](https://pypi.org/project/graphviz/) package:

```python
import graphviz

graphviz.Source.from_file("seq.dot").render("seq", format="svg")
```

## Read the figure

The DOT file describes nested boxes:

- the outer boxes are the **sub-sequences** of the sequence (a sequence is split into
  sub-sequences when it contains control flow, such as switches or loops);
- inside, each box is a **module**, labelled with its name and its execution order
  (`exec order`);
- inside a module, each box is a **task**, labelled with its name and its id;
- inside a task, each node is a **socket**, labelled with its direction, its index and
  its name: `in[0]:in`, `out[1]:out`, `fwd[0]:data`…;
- the arrows are the **bindings** between sockets.

Reading the execution order of the modules is a good way to check that a graph runs
the tasks in the expected order.
