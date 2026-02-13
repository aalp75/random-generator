from setuptools import setup, Extension, find_packages
import pybind11

ext_modules = [
    Extension(
        "rngcpp",
        [
            "src/cpp/bindings.cpp",
            "src/cpp/mt19937.cpp",
            "src/cpp/middle_square.cpp",
            "src/cpp/congruence.cpp",
        ],
        include_dirs=[pybind11.get_include()],
        language="c++",
    )
]

setup(
    name="rng",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    ext_modules=ext_modules,
)
