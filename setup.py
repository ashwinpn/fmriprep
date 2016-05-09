#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: oesteban
# @Date:   2015-11-19 16:44:27
# @Last Modified by:   oesteban
# @Last Modified time: 2016-04-20 14:34:36
""" fmriprep setup script """
import os
import sys

from fmriprep import __version__, __email__, __url__, __packagename__, __license__


REQ_LINKS = []
with open('requirements.txt', 'r') as rfile:
    REQUIREMENTS = [line.strip() for line in rfile.readlines()]

for i, req in enumerate(REQUIREMENTS):
    if req.startswith('-e'):
        REQUIREMENTS[i] = req.split('=')[1]
        REQ_LINKS.append(req.split()[1])

if REQUIREMENTS is None:
    REQUIREMENTS = []

def main():
    """ Install entry-point """
    from glob import glob
    from setuptools import setup

    setup(
        name=__packagename__,
        version=__version__,
        description='',
        author_email=__email__,
        url=__url__,
        download_url='https://pypi.python.org/packages/source/f/fmriprep/'
                     'fmriprep-%s.tar.gz' % __version__,
        license=__license__,
        entry_points={'console_scripts': ['fmriprep=fmriprep.run_workflow:main',]},
        packages=['fmriprep', 'fmriprep.workflows', 'fmriprep.viz'],
        package_data={'fmriprep': ['data/*.nii.gz']},
        install_requires=REQUIREMENTS,
        dependency_links=REQ_LINKS,
        zip_safe=False,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: MRI processing',
            'Topic :: Scientific/Engineering :: Biomedical Imaging',
            'License :: OSI Approved :: 3-clause BSD License',
            'Programming Language :: Python :: 2.7',
        ],
    )

if __name__ == '__main__':
    local_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(local_path)
    sys.path.insert(0, local_path)

    main()