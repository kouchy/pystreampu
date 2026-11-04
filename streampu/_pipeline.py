# -*- coding: utf-8 -*-
from streampu._ext.core import _Pipeline


class Pipeline(_Pipeline):
    """Overlay of streampu._ext.core._Pipeline."""

    def __init__(self, *args, **kwargs):
        """Build a Pipeline.

        The arguments are those of the C++ constructor, in this order: `firsts` (first
        tasks), `lasts` (last tasks), `sep_stages` (for each stage, a list
        `[first tasks, last tasks, excluded tasks]`), `n_threads` (number of threads per
        stage), `synchro_buffer_sizes` and `synchro_active_waiting` (one value between
        each pair of consecutive stages), `thread_pinning` and `puids`.

        Args:
            *args (Any): positional arguments of the C++ constructor
            **kwargs (Any): keyword arguments of the C++ constructor

        Examples:
            >>> pipeline = streampu.Pipeline(
            ...     [source.generate], [sink.send_count],
            ...     [[[source.generate], [source.generate], []],
            ...      [[rly.relay], [rly.relay], []],
            ...      [[sink.send_count], [sink.send_count], []]],
            ...     [1, 4, 1], [16, 16], [False, False])
            >>> pipeline.exec()
        """
        super().__init__(*args, **kwargs)
        self.original_modules = super().get_original_modules()

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
