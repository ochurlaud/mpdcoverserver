#!/usr/bin/python3

from setuptools import setup, find_packages
setup(
    name="MPDCoverServer",
    version="0.1",
    install_requires=['mutagen'],
    author="Olivier Churlaud",
    author_email="olivier@churlaud.com",
    license="GPLv3",
    keywords="mpd covers mutagen",
    description="Server that provides covers from the music files to MPD clients",
    scripts=["src/mpdcoverserver"],
    packages=['songcovers'],
    package_dir={'songcovers': 'src/songcovers'},
)
