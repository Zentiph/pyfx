"""Abstract superclasses for pyfx effects."""

from abc import ABC, abstractmethod

from .argval import enforce_arg_within, enforce_type
from .enums import Alignment
from .exceptions import DuplicateChildError


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
        :type to: PIL.ImageDraw.ImageDraw
        """

        raise NotImplementedError("Subclasses should implement this!")


class FXGroup(FXNode):
    """Group of FXNodes."""

    def __init__(self, *nodes):
        """Initialize the FXGroup with a list of FXNodes.

        :param nodes: List of FXNode instances
        :type nodes: Tuple[pyfx.FXNode]
        """

        for node in nodes:
            if not isinstance(node, FXNode):
                raise TypeError("All nodes must be instances of FXNode")

        super().__init__()
        self._nodes = set(nodes)

    @enforce_type("node", FXNode)
    def add(self, node):
        """Add an FXNode to the group.

        :param node: FXNode instance to add
        :type node: pyfx.FXNode
        """

        if node in self._nodes:
            raise DuplicateChildError("Node already exists in the group")
        self._nodes.add(node)

    @enforce_type("node", FXNode)
    def remove(self, node):
        """Remove an FXNode from the group.

        :param node: FXNode instance to remove
        :type node: pyfx.FXNode
        """

        if node in self._nodes:
            self._nodes.remove(node)

    def contains(self, node):
        """Check if the group contains a specific FXNode.

        :param node: FXNode instance to check
        :type node: pyfx.FXNode
        :return: True if the node is in the group, False otherwise
        :rtype: bool
        """

        return node in self._nodes

    def render(self, to):
        """Render this group by rendering all FXNodes in the group.

        :param to: Output destination for the rendered effects
        :type to: PIL.ImageDraw.ImageDraw
        """

        for node in self._nodes:
            node.render(to)

    def __iter__(self):
        """Iterate over the FXNodes in the group.

        :return: Iterator over the FXNodes
        :rtype: Iterator[pyfx.FXNode]
        """

        return iter(self._nodes)
