"""Configure doctesting by pytest."""

import importlib

import cv2
import pytest


@pytest.fixture(autouse=True)
def doctest_pre_code(doctest_namespace):
    """Import modules for doctesting.

    This fixture is equivalent to::

        import cv2
        from finitedepth import *
    """
    doctest_namespace["cv2"] = cv2

    mod = importlib.import_module("finitedepth")
    for var in mod.__all__:
        doctest_namespace[var] = getattr(mod, var)
