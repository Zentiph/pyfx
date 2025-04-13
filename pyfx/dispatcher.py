"""Module for dispatching FXNodes to output files."""

from PIL import Image, ImageDraw

from .argval import enforce_type
from .containers import Canvas
from .supers import FXGroup


class Dispatcher:
    """Exports FXNodes to output files."""

    @enforce_type("canvas", Canvas)
    def __init__(self, canvas):
        """Initialize the Dispatcher with a Canvas.

        :param canvas: The canvas containing FXNodes to export
        :type canvas: pyfx.Canvas
        """

        self._canvas = canvas
        self._image = Image.new("RGBA", canvas.size, [*canvas.bg_color, 1])
        self._drawer = ImageDraw.Draw(self._image)

    @enforce_type("output_path", str)
    def export(self, output_path):
        """Export the canvas to an image file.

        :param output_path: Path to the output image file
        :type output_path: str
        """

        if isinstance(self._canvas.root, FXGroup):
            for node in self._canvas.root:
                node.render(self._canvas)
        else:
            self._canvas.root.render(self._image)

        self._image.save(output_path)
