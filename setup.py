from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="s2p-plugins",
    version="0.01",
    author="HaoRan Chang",
    author_email="haoran.chang@mail.mcgill.ca",
    description="A set of plugins for suite2p used at the McNaughton Lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LelouchLamperougeVI/s2p-plugins",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        'suite2p.plugin': [
            'smooth_dff = smooth_dff.smooth_dff:smooth_dff',
        ],
    }
)
