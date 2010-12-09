#!/usr/bin/env python

from distutils.core import setup

setup (name = "monoprocessing",
       version = "0.1",
       description = "A dummy implementation of multiprocessing.Pool",
       long_description = 
"""monoprocessing.Pool is a dummy version of multiprocessing.Pool. It
executes all tasks immediately in the same process. This is useful
when testing or debugging the logic of a parallelized program.""",
       author = "Konrad Hinsen",
       author_email = "konrad.hinsen@cnrs-orleans.fr",
       license = "CeCILL-C",
       url = "http://bitbucket.org/khinsen/monoprocessing",
       py_modules = ['monoprocessing'],
       )
