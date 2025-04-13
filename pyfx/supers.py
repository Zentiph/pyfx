"""Abstract superclasses for pyfx effects."""

from abc import ABC, abstractmethod

from .argval import enforce_arg_within, enforce_type
from .enums import Alignment


class FXNode(ABC):
    """Abstract base class for all FX nodes.
    This class defines the interface for creating visual effects nodes.
    """

    def __init__(self):
        """Initialize the FXNode."""

        self._alignment = Alignment.CENTER_LEFT
        self._opacity = 1.0

    @property
    def alignment(self):
        """Get the alignment of the effect node.

        :return: Alignment value
        :rtype: pyfx.Alignment
        """

        return self._alignment

    @alignment.setter
    @enforce_type("alignment", Alignment)
    def alignment(self, alignment):
        """Set the alignment of the effect node.

        :param alignment: Alignment value
        :type alignment: pyfx.Alignment
        """

        self._alignment = alignment

    @property
    def opacity(self):
        """Get the opacity of the effect node.

        :return: Opacity value
        :rtype: float
        """

        return self._opacity

    @opacity.setter
    @enforce_arg_within("opacity", 0.0, 1.0)
    @enforce_type("opacity", float)
    def opacity(self, opacity):
        """Set the opacity of the effect node.

        :param opacity: Opacity value
        :type opacity: float
        """

        self._opacity = opacity

    @abstractmethod
    def render(self, to):
        """Render the effect node.
        This method should be implemented by subclasses to render the effect.

        :param to: Output destination for the rendered effect
        :type to: Any
        """

        raise NotImplementedError("Subclasses should implement this!")
