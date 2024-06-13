.. DipCoatImage-FiniteDepth-IFD documentation master file, created by
   sphinx-quickstart on Wed Jun  5 17:47:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. currentmodule:: finitedepth_ifd

DipCoatImage-FiniteDepth-IFD documentation
==========================================

.. plot:: plot-header.py
    :include-source: False

DipCoatImage-FiniteDepth-IFD is a Python package to analyze
coating layer roughness with integral Fréchet distance (IFD) in
finite depth dip coating.

Installation
------------

DipCoatImage-FiniteDepth-IFD can be downloaded from
`PyPI <https://pypi.org/project/dipcoatimage-finitedepth-ifd/>`_ by
using :mod:`pip`::

   pip install dipcoatimage-finitedepth-ifd

You can also install with optional dependencies as::

   pip install dipcoatimage-finitedepth-ifd[dev]

Available optional dependencies for DipCoatImage-FiniteDepth are:

* ``test``: run unit test and doctest.
* ``doc``: build documentation.
* ``dev``: every dependency (for development).

Usage
-----

DipCoatImage-FiniteDepth-IFD provides :class:`IfdRoughnessBase`, which is an
an abstract base class that implements IFD-based roughness computation.
You can either subclass it to define your own implementation, or use
pre-defined concrete class such as :class:`RectIfdRoughness`.

You can use your class as a standard *coating layer* class in both Python
runtime or in an analysis configuration file for command-line invocation.
Refer to `DipCoatImage-FiniteDepth`_ documentation for more information.

.. _DipCoatImage-FiniteDepth: https://pypi.org/project/dipcoatimage-finitedepth/

API reference
-------------

.. automodule:: finitedepth_ifd
    :members:

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
