"""Configure doctesting by pytest."""

import cv2
import finitedepth
import pytest

import finitedepth_ifd


@pytest.fixture(autouse=True)
def doctest_pre_code(doctest_namespace):
    """Import modules for doctesting.

    This fixture is equivalent to::

        import cv2
        from finitedepth import *
    """
    doctest_namespace["cv2"] = cv2
    for var in finitedepth.__all__:
        doctest_namespace[var] = getattr(finitedepth, var)


@pytest.fixture()
def RectIfdRoughness_setup():
    ref_img = cv2.imread(finitedepth.get_sample_path("ref.png"), cv2.IMREAD_GRAYSCALE)
    ref = finitedepth.Reference(
        cv2.threshold(ref_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1],
        (10, 10, 1250, 200),
        (100, 100, 1200, 500),
    )
    subst = finitedepth.RectSubstrate(ref, 3.0, 1.0, 0.01)
    target_img = cv2.imread(
        finitedepth.get_sample_path("coat.png"), cv2.IMREAD_GRAYSCALE
    )
    coat = finitedepth_ifd.RectIfdRoughness(
        cv2.threshold(target_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1],
        subst,
        "arithmetic",
        5.0,
        (1, 1),
        50,
    )
    return coat
