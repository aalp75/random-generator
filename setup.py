from setuptools import setup, Extension, find_packages
import pybind11
import sysconfig

python_inc = sysconfig.get_paths()["include"]

ext_modules = [
    Extension(
        "rng.rngcpp",
        [
            "src/cpp/bindings.cpp",
            "src/cpp/mt19937.cpp",
            "src/cpp/middle_square.cpp",
            "src/cpp/congruence.cpp",
        ],
        include_dirs=[pybind11.get_include(), python_inc],
        language="c++",
        extra_compile_args=["-O3", "-std=c++20"]
    )
]

setup(
    name="rng",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    ext_modules=ext_modules,
)
