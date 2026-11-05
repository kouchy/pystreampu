#ifndef WRAPPER_JULIA_GC_REGION_HPP_
#define WRAPPER_JULIA_GC_REGION_HPP_

// Cohabitation of the GIL of Python and of the garbage collector (GC) of Julia.
//
// The threads of a Sequence or Pipeline that contains Julia modules are adopted by Julia.
// When the GC of Julia runs, it waits for all the adopted threads to be at a safepoint or in
// a GC-safe region. A thread that waits for the GIL, or runs Python code, never reaches a
// safepoint: it must be in a GC-safe region, otherwise the GC (and every Julia thread) waits
// for it, or deadlocks with the thread that holds the GIL.
//
// Julia_gc_safe_region: enter a GC-safe region if the thread is adopted by Julia (no Julia
// object may be used inside).
// Julia_gc_unsafe_region: the opposite, to call the Julia C API (from Python code that runs in
// a GC-safe region, or from a thread that Julia does not know yet: it is adopted).
// Without Julia (SPU_JULIA undefined), both do nothing.

#ifdef SPU_JULIA
#include <julia.h>
#endif

namespace pyspu
{
namespace wrapper
{
#ifdef SPU_JULIA
class Julia_gc_safe_region
{
    int8_t state = 0;
    bool active = false;

  public:
    Julia_gc_safe_region()
    {
        if (jl_is_initialized() && jl_get_pgcstack() != nullptr)
        {
            this->state = jl_gc_safe_enter(jl_current_task->ptls);
            this->active = true;
        }
    }
    ~Julia_gc_safe_region()
    {
        if (this->active) jl_gc_safe_leave(jl_current_task->ptls, this->state);
    }
    Julia_gc_safe_region(const Julia_gc_safe_region&) = delete;
    Julia_gc_safe_region& operator=(const Julia_gc_safe_region&) = delete;
};

class Julia_gc_unsafe_region
{
    int8_t state = 0;
    bool active = false;

  public:
    Julia_gc_unsafe_region()
    {
        if (!jl_is_initialized()) return;
        if (jl_get_pgcstack() == nullptr) jl_adopt_thread(); // thread unknown to Julia
        this->state = jl_gc_unsafe_enter(jl_current_task->ptls);
        this->active = true;
    }
    ~Julia_gc_unsafe_region()
    {
        if (this->active) jl_gc_unsafe_leave(jl_current_task->ptls, this->state);
    }
    Julia_gc_unsafe_region(const Julia_gc_unsafe_region&) = delete;
    Julia_gc_unsafe_region& operator=(const Julia_gc_unsafe_region&) = delete;
};
#else
struct Julia_gc_safe_region
{
};
struct Julia_gc_unsafe_region
{
};
#endif
} // namespace wrapper
} // namespace pyspu

#endif // WRAPPER_JULIA_GC_REGION_HPP_
