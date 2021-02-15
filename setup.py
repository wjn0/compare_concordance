import setuptools

from distutils.extension import Extension


compareC = Extension('compareC',
                     sources=['src/compareC.c'],
                     extra_compile_args=['-fPIC'])

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compare_concordance", # Replace with your own username
    version="0.0.1",
    author="Walter Nelson",
    author_email="walterj.nelson@mail.utoronto.ca",
    description="Statistical inference about right-censored c-indices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wjn0/compare_concordance",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["compare_concordance"],
    ext_modules=[compareC],
    data_files=[("compare_concordance", ["build/lib.linux-x86_64-3.6/compareC.cpython-36m-x86_64-linux-gnu.so"])]
)
