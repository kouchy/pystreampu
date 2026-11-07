# -*- coding: utf-8 -*-
from typing import List, Tuple

from streampu._ext.core import Task, _Pipeline


class Pipeline(_Pipeline):
    """Graph of tasks split into stages that run at the same time."""

    def __init__(
        self,
        firsts: List[Task],
        lasts: List[Task],
        sep_stages: List[Tuple[List[Task], List[Task], List[Task]]] = (),
        n_threads: List[int] = (),
        synchro_buffer_sizes: List[int] = (),
        synchro_active_waiting: List[bool] = (),
        thread_pinning: List[bool] = (),
        puids: List[List[int]] = (),
    ):
        """Build a pipeline: a graph split into stages that run at the same time.

        Each stage is a sequence with its own threads. Two consecutive stages exchange the
        frames through a buffer: while a stage processes a frame, the previous one already
        processes the next frames. The lists `sep_stages`, `n_threads` and
        `thread_pinning` have one element per stage, `synchro_buffer_sizes` and
        `synchro_active_waiting` one element per pair of consecutive stages.

        Args:
            firsts (list[Task]): first tasks of the whole graph
            lasts (list[Task]): last tasks of the whole graph
            sep_stages (list): for each stage, `[first tasks, last tasks, excluded tasks]`
                of the stage (as for `Sequence(firsts, lasts, exclusions)`)
            n_threads (list[int]): number of threads of each stage; a stage with more than
                one thread must not contain a task that keeps a state between frames
                (e.g. a source that reads a file)
            synchro_buffer_sizes (list[int]): number of frames that the buffer between two
                consecutive stages can hold
            synchro_active_waiting (list[bool]): for each buffer, wait for it in a loop
                (True: lower latency, but a core is busy) or asleep (False)
            thread_pinning (list[bool]): pin the threads of each stage (needs StreamPU
                built with hwloc)
            puids (list[list[int]]): for each stage, the processing unit of each thread

        Examples:
            A source, a relay on 4 threads and a sink, in three stages:

            >>> pipeline = streampu.Pipeline(
            ...     [src.generate],                          # firsts
            ...     [snk.send_count],                        # lasts
            ...     [                                        # sep_stages
            ...         [[src.generate], [src.generate], []],
            ...         [[rly.relay], [rly.relay], []],
            ...         [[snk.send_count], [snk.send_count], []],
            ...     ],
            ...     [1, 4, 1],                               # n_threads
            ...     [16, 16],                                # synchro_buffer_sizes
            ...     [False, False],                          # synchro_active_waiting
            ... )
            >>> pipeline.exec()
        """
        super().__init__(
            firsts,
            lasts,
            list(sep_stages),
            list(n_threads),
            list(synchro_buffer_sizes),
            list(synchro_active_waiting),
            list(thread_pinning),
            list(puids),
        )
        self.original_modules = super().get_original_modules()
        """Modules created by the user, one list per stage (without the clones and adaptors)."""

    def __del__(self):
        """Destructor."""
        self.unbind_adaptors()

    def get_modules(self, module_class: type, set_modules: bool = True) -> list:
        """Return the list of modules of a given class.

        Args:
            module_class(type): a module class type
            set_modules(bool): if True consider 'set' as modules,
                else explore the content of the set

        Returns:
            out (list): list of modules with type `module_class`
        """
        return_list = []
        for stage in self.stages:
            modules = stage.get_modules(module_class, set_modules)
            return_list.extend(modules)
        return return_list


__all__ = ["Pipeline"]
