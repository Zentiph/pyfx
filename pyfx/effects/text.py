"""Text effect."""

from PIL import ImageFont

from ..argval import enforce_type


class Text:
    """Class for rendering text effects."""

    @enforce_type("text", str)
    @enforce_type("position", tuple)
    @enforce_type("font", str)
    @enforce_type("font_size", int)
    @enforce_type("color", (str, tuple))
    @enforce_type("highlight_color", (str, tuple, type(None)))
    def __init__(
        self,
        text,
        position=(0, 0),
        font="Arial",
        font_size=20,
        color="white",
        highlight_color=None,
    ):
        """Initialize the Text effect.

        :param text: The text to render
        :type text: str
        :param position: The position to render the text (x, y)
        :type position: Tuple[int, int]
        :param font: The font to use
        :type font: str
        :param font_size: The size of the font
        :type font_size: int
        :param color: The color of the text
        :type color: str | Tuple[int, int, int]
        :param highlight_color: The highlight color for the text
        :type highlight_color: str | Tuple[int, int, int] | None
        """

        if len(position) != 2:
            raise ValueError("Position must be a tuple of (x, y)")
        for dim in position:
            if not isinstance(dim, int):
                raise ValueError("Position dimensions must be integers")

        self._text = text
        self._position = position
        self._font = (
            ImageFont.truetype(font + ".ttf", font_size)
            if font
            else ImageFont.load_default(font_size)
        )
        self._color = color
        self._highlight_color = highlight_color

    @property
    def text(self):
        """Get the text to render.

        :return: The text
        :rtype: str
        """

        return self._text

    @property
    def position(self):
        """Get the position of the text.

        :return: The position as a tuple (x, y)
        :rtype: Tuple[int, int]
        """

        return self._position

    @property
    def font(self):
        """Get the font used for the text.

        :return: The font
        :rtype: PIL.ImageFont.FreeTypeFont | PIL.ImageFont.ImageFont
        """

        return self._font

    @property
    def color(self):
        """Get the color of the text.

        :return: The color
        :rtype: str | Tuple[int, int, int]
        """

        return self._color

    @property
    def highlight_color(self):
        """Get the highlight color of the text.

        :return: The highlight color
        :rtype: str | Tuple[int, int, int] | None
        """

        return self._highlight_color

    def render(self, draw):
        """Render the text to the image.

        :param draw: The image to render to
        :type draw: PIL.ImageDraw.ImageDraw
        """

        text_size = draw.textsize(self._text, font=self._font)

        if self._highlight_color:
            x, y = self._position
            draw.rectangle(
                [x, y, x + text_size[0] + 10, y + text_size[1] + 10],
                fill=self._highlight_color,
            )

        draw.text(
            (self._position[0] + 5, self._position[1] + 5),
            self._text,
            fill=self._color,
            font=self._font,
        )
