"""Canvas for rendering a scene in PyFX."""

from PIL import Image, ImageDraw

from ..argval import enforce_type
from ..supers import FXNode


class Canvas:
    """Class representing a canvas for rendering effects."""

    @enforce_type("bg_color", (str, tuple))
    @enforce_type("size", tuple)
    @enforce_type("root", FXNode)
    def __init__(self, root, size=(1280, 720), bg_color="black"):
        """Initialize the canvas with a given size and background color.

        :param root: Root FXNode for the canvas
        :type root: FXNode
        :param size: Size of the canvas as a tuple (width, height)
        :type size: Tuple[int, int]
        :param bg_color: Background color of the canvas
        :type bg_color: str | Tuple[int, int, int]
        """

        if len(size) != 2:
            raise ValueError("Size must be a tuple of (width, height)")
        for dim in size:
            if not isinstance(dim, int) or dim <= 0:
                raise ValueError("Size dimensions must be positive integers")

        self._root = root
        self._size = size
        self._bg_color = bg_color
        self._canvas = Image.new("RGBA", self.size, [*self.bg_color, 1])
        self._drawer = ImageDraw.Draw(self._canvas)

    @property
    def root(self):
        """Get the root FXNode of the canvas.

        :return: Root FXNode
        :rtype: FXNode
        """

        return self._root

    @property
    def size(self):
        """Get the size of the canvas.

        :return: Size of the canvas as a tuple (width, height)
        :rtype: Tuple[int, int]
        """

        return self._size

    @property
    def bg_color(self):
        """Get the background color of the canvas.

        :return: Background color
        :rtype: str | Tuple[int, int, int]
        """

        return self._bg_color
