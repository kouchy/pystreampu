# Julia code of the modules of julia_module.py: types of the states and codelets.
#
# A codelet receives, in this order: the states of the module (Stateful_Julia only), the
# sockets of the task (1D vectors, without copy), the constants of the task, then
# `frame_id` and `n_frames_per_wave` (UInt32). It returns 0 on success.

# State of the module `acc`: sum of all the samples it has received
mutable struct Accumulator
    total::Int64
    calls::Int64
end

# Shared configuration (the clones of a Sequence share the same object)
struct Gain
    factor::Int32
end

function accumulate(acc::Accumulator, gain::Gain, sck_in, sck_out, rnt_frame_id, rnt_n_frames_per_wave)
    acc.calls += 1
    @inbounds for i in eachindex(sck_in)
        acc.total += sck_in[i]
        sck_out[i] = sck_in[i] * gain.factor
    end
    return 0
end
