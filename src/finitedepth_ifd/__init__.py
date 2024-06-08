"""Finite depth dip coating uniformity measurement using integral Fréchet distance."""

import abc

import numpy as np
import numpy.typing as npt
from curvesimilarities import afd_owp, qafd_owp  # type: ignore[import-untyped]
from finitedepth import CoatingLayerBase, SubstrateBase

__all__ = [
    "IfdRoughnessBase",
]


AVERAGE_TYPES = (
    "arithmetic",
    "quadratic",
)


class IfdRoughnessBase(CoatingLayerBase):
    """Base class for layer roughness measurement with integral Fréchet distance."""

    def __init__(
        self,
        image: npt.NDArray[np.uint8],
        substrate: SubstrateBase,
        average_type: str,
        delta: float,
        *,
        tempmatch: tuple[tuple[int, ...], float] | None = None,
    ):
        """Check parameter types and values."""
        if average_type not in AVERAGE_TYPES:
            raise ValueError("Unknown average type: %s" % average_type)
        if not isinstance(delta, float):
            raise TypeError("delta must be a double-precision float.")
        if not delta > 0:
            raise TypeError("delta must be a positive number.")
        super().__init__(image, substrate, tempmatch=tempmatch)
        self.average_type = average_type
        self.delta = delta

    @abc.abstractmethod
    def surface(self) -> npt.NDArray[np.int32]:
        """Coating layer surface."""
        ...

    @abc.abstractmethod
    def uniform_layer(self) -> npt.NDArray[np.float_]:
        """Imaginary, ideal uniform layer."""
        ...

    def roughness(self) -> tuple[float, npt.NDArray[np.float_]]:
        """Integral Fréchet distance-based surface roughness of the coating layer."""
        if self.average_type == "arithmetic":
            roughness, path = afd_owp(self.surface(), self.uniform_layer(), self.delta)
        elif self.average_type == "quadratic":
            roughness, path = qafd_owp(self.surface(), self.uniform_layer(), self.delta)
        else:
            roughness, path = np.nan, np.empty((0, 2), dtype=np.float_)
        return float(roughness), path
