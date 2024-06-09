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
    """Base class for layer roughness measurement with integral Fréchet distance.

    Roughness can be measured by the similarity between the coating layer profile
    and the ideal uniform layer profile. In arbitrary geometries, the following
    integral-based average distances are used:

    - Arithmetic roughness :math:`R_a` : average Fréchet distance.
    - Quadratic mean roughness :math:`R_q` : quadratic average Fréchet distance.

    Refer to the See Also section for more information about these distances.

    Parameters
    ----------
    image, substrate
        See :class:`CoatingLayerBase <finitedepth.CoatingLayerBase>`.
    average_type : {'arithmetic', 'quadratic'}
        The type of average Fréchet distance to compute the roughness, either the
        arithmetic average or the quadratic mean.
    delta : double
        The maximum distance between the Steiner points to compute the roughness.
        Refer to the functions in the See Also section.

    Other Parameters
    ----------------
    tempmatch : tuple, optional
        See :class:`CoatingLayerBase <finitedepth.CoatingLayerBase>`.

    See Also
    --------
    curvesimilarities.averagefrechet.afd : Average Fréchet distance.
    curvesimilarities.averagefrechet.qafd : Quadratic average Fréchet distance.
    """

    def __init__(
        self,
        image: npt.NDArray[np.uint8],
        substrate: SubstrateBase,
        average_type: str,
        delta: float,
        *,
        tempmatch: tuple[tuple[int, int], float] | None = None,
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
        """Coating layer surface.

        Returns
        -------
        ndarray
            An :math:`N` by :math:`2` array containing the :math:`xy`-coordinates
            of :math:`N` points which constitute the coating layer surface curve.
        """
        ...

    @abc.abstractmethod
    def uniform_layer(self) -> npt.NDArray[np.float_]:
        """Imaginary, ideal uniform layer.

        Returns
        -------
        ndarray
            An :math:`M` by :math:`2` array containing the :math:`xy`-coordinates
            of :math:`M` points which constitute the uniform layer curve.
        """
        ...

    def roughness(self) -> tuple[float, npt.NDArray[np.float_]]:
        """Surface roughness of the coating layer.

        The roughness is acquired by computing the similarity between
        :meth:`surface` and :meth:`uniform_layer`.

        Returns
        -------
        roughness : double
            Roughness value.
        path : ndarray
            An :math:`P` by :math:`2` array representing the optimal warping path
            in the parameter space.
        """
        if self.average_type == "arithmetic":
            roughness, path = afd_owp(self.surface(), self.uniform_layer(), self.delta)
        elif self.average_type == "quadratic":
            roughness, path = qafd_owp(self.surface(), self.uniform_layer(), self.delta)
        else:
            roughness, path = np.nan, np.empty((0, 2), dtype=np.float_)
        return float(roughness), path
