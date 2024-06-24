import cv2
import matplotlib.pyplot as plt
from finitedepth import RectSubstrate, Reference, get_sample_path

from finitedepth_ifd import RectIfdRoughness

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
_, path = coat.roughness()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].imshow(coat.draw()[200:650, 200:1100])
axes[0].set_title("Curve space")
for sp in axes[0].spines:
    axes[0].spines[sp].set_visible(False)
axes[0].xaxis.set_visible(False)
axes[0].yaxis.set_visible(False)

axes[1].plot(*path.T)
axes[1].set_title("Parameter space")
(x0, y0), (x1, y1) = path[[0, -1]]
axes[1].set_xlim(left=x0, right=x1)
axes[1].set_ylim(bottom=y0, top=y1)
axes[1].xaxis.set_visible(False)
axes[1].yaxis.set_visible(False)
axes[1].set_aspect("equal")

fig.tight_layout()
