from setuptools import find_packages, setup

from distutils.extension import Extension
from distutils.command.build_ext import build_ext as build_ext_orig


# From: https://github.com/himbeles/ctypes-example/blob/master/setup.py
class CTypesExtension(Extension):
    pass


class build_ext(build_ext_orig):
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypesExtension)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + ".so"
        return super().get_ext_filename(ext_name)


compareC = CTypesExtension("compare_concordance.compareC",
                           sources=["compare_concordance/compareC.c"],
                           extra_compile_args=["-fPIC"])

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="compare_concordance",
    version="0.0.1",
    author="Walter Nelson",
    author_email="walterj.nelson@mail.utoronto.ca",
    description="Statistical inference about right-censored c-indices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wjn0/compare_concordance",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    ],
    python_requires=">=3.6",
    py_modules=["compare_concordance"],
    ext_modules=[compareC],
    cmdclass={"build_ext": build_ext},
)
