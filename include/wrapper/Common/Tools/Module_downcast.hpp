/*!
 * \file
 * \brief Typing of the `spu::module::Module*` returned to Python, extensible by the extension modules.
 *
 * pybind11 types a returned `Module*` after its dynamic type: when this exact class is not registered (a concrete
 * class of an extension that only registers its abstract bases, e.g. AFF3CT), the object falls back to the static
 * type `Module` and loses the methods of its registered bases. This header specializes
 * `pybind11::polymorphic_type_hook<spu::module::Module>`: when the dynamic type is not registered, the downcasters
 * registered by the extensions are asked for the most derived registered class of the object.
 *
 * The registry is stored in the pybind11 internals (`get_shared_data`), shared by every extension built with the
 * same pybind11 ABI, so it works although each extension links its own copy of the static StreamPU library.
 *
 * Usage in an extension (once, at import, after its classes are registered):
 * \code
 * #include "wrapper/Common/Tools/Module_downcast.hpp"
 *
 * static const void* my_downcaster(const spu::module::Module* m, const std::type_info*& type)
 * {
 *     // most derived first
 *     if (auto p = pyspu::downcast_to<My_concrete_base<int>>(m, type)) return p;
 *     if (auto p = pyspu::downcast_to<My_base>(m, type)) return p;
 *     return nullptr;
 * }
 * PYBIND11_MODULE(my_ext, m) { ...; pyspu::register_module_downcaster(&my_downcaster); }
 * \endcode
 *
 * This header must be seen by every translation unit that casts a `spu::module::Module*` (ODR): pystreampu includes
 * it from "wrapper/Common/pybind11_common.h"; an extension includes it with its own pybind11 headers.
 */
#ifndef WRAPPER_COMMON_TOOLS_MODULE_DOWNCAST_HPP_
#define WRAPPER_COMMON_TOOLS_MODULE_DOWNCAST_HPP_

#include <mutex>
#include <typeinfo>
#include <vector>

#include <pybind11/pybind11.h>

#include <Module/Module.hpp>

//! Defined when pystreampu provides the Module downcast registry (feature test for the extensions).
#define PYSPU_HAS_MODULE_DOWNCAST_REGISTRY 1

namespace pyspu
{
/*!
 * \brief Returns a pointer to the most derived registered class of `m` known by the downcaster (and sets `type` to
 *        its `typeid`), or nullptr (then `type` is left unchanged).
 */
using module_downcaster = const void* (*)(const spu::module::Module* m, const std::type_info*& type);

namespace detail
{
struct module_downcast_registry
{
    std::mutex mutex; // the registration (import) can race with casts in free-threaded Python
    std::vector<module_downcaster> downcasters;
};

//! Registry shared by every extension module (versioned key: the layout of the struct is part of the ABI).
inline module_downcast_registry&
get_module_downcast_registry()
{
    static constexpr const char* key = "pystreampu_module_downcast_registry_v1";
    auto* reg = static_cast<module_downcast_registry*>(pybind11::get_shared_data(key));
    if (reg == nullptr)
        reg = static_cast<module_downcast_registry*>(pybind11::set_shared_data(key, new module_downcast_registry()));
    return *reg;
}
} // namespace detail

//! Registers a downcaster (called by the extensions at import, the GIL being held).
inline void
register_module_downcaster(module_downcaster downcaster)
{
    auto& reg = detail::get_module_downcast_registry();
    std::lock_guard<std::mutex> lock(reg.mutex);
    reg.downcasters.push_back(downcaster);
}

//! Downcaster step for a registered class `T`: `dynamic_cast` (to be tried from the most derived class).
template<class T>
const void*
downcast_to(const spu::module::Module* m, const std::type_info*& type)
{
    if (auto p = dynamic_cast<const T*>(m))
    {
        type = &typeid(T);
        return p;
    }
    return nullptr;
}

//! Most derived registered class of `m` according to the registered downcasters (nullptr if none knows `m`).
inline const void*
downcast_module(const spu::module::Module* m, const std::type_info*& type)
{
    auto& reg = detail::get_module_downcast_registry();
    std::lock_guard<std::mutex> lock(reg.mutex);
    // the last registered extension first: an extension built on top of another one knows more derived classes
    for (auto it = reg.downcasters.rbegin(); it != reg.downcasters.rend(); ++it)
        if (auto p = (*it)(m, type)) return p;
    return nullptr;
}
} // namespace pyspu

namespace pybind11
{
template<>
struct polymorphic_type_hook<spu::module::Module>
{
    static const void* get(const spu::module::Module* src, const std::type_info*& type)
    {
        if (src == nullptr) return src;
        const std::type_info& dynamic_type = typeid(*src);
        // registered dynamic type: default pybind11 behavior
        if (detail::get_type_info(dynamic_type) == nullptr)
            if (auto p = pyspu::downcast_module(src, type)) return p;
        type = &dynamic_type;
        return dynamic_cast<const void*>(src);
    }
};
} // namespace pybind11

#endif // WRAPPER_COMMON_TOOLS_MODULE_DOWNCAST_HPP_
