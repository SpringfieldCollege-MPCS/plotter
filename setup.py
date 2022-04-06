import setuptools


setuptools.setup(
    name="plotter",
    version="0.0.1",
    install_requires=[
        'matplotlib',
      ],
    entry_points = {
        'console_scripts': ['plot=plotter.commandline:main'],
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)