import setuptools


setuptools.setup(
    name="plotter",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    long_description="",
    url="",
    install_requires=[
        'matplotlib',
      ],
    # entry_points = {
    #     'console_scripts': ['plot=plotter.command_line:main'],
    # },
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)