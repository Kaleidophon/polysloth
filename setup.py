"""
Installing the module locally.
"""
from setuptools import setup
from polysloth import __version__

setup(
    name="polysloth",
    version=__version__,
    description="Creating Anki-importable files with new vocabulary"\
                "based on the PONS-API and your Todoist-Lists",
    url="https://github.com/Kaleidophon/polysloth",
    author="Kaleidophon",
    license="MIT",
    packages=["polysloth"],
    zip_safe=False
)
