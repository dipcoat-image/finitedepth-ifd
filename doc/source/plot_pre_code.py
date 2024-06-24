import cv2
from finitedepth import RectSubstrate, Reference, get_sample_path

from finitedepth_ifd import RectIfdRoughness


def RectIfdRoughness_setup():
    ref_img = cv2.imread(get_sample_path("ref.png"), cv2.IMREAD_GRAYSCALE)
    ref = Reference(
        cv2.threshold(ref_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1],
        (10, 10, 1250, 200),
        (100, 100, 1200, 500),
    )
    subst = RectSubstrate(ref, 3.0, 1.0, 0.01)
    target_img = cv2.imread(get_sample_path("coat.png"), cv2.IMREAD_GRAYSCALE)
    coat = RectIfdRoughness(
        cv2.threshold(target_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1],
        subst,
        5.0,
        (1, 1),
        50,
    )
    return coat


coat = RectIfdRoughness_setup()


def getfixture(argname):
    # Make both pytest and plot directive work
    return globals()[argname]()
