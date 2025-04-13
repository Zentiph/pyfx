"""FXGroup class for grouping FXNodes."""

from ..argval import enforce_type
from ..exceptions import DuplicateChildError
from ..supers import FXNode


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
        :type to: Any
        """

        for node in self._nodes:
            node.render(to)
