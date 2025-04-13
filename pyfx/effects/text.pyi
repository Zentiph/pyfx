# pylint: disable=all

import PIL
import PIL.ImageDraw

from typing import Tuple, Union

import PIL.ImageFont

class Text:
    """Class for rendering text effects."""

    def __init__(
        self,
        text: str,
        position: Tuple[int, int] = (0, 0),
        font: str = "Arial",
        font_size: int = 20,
        color: Union[str, Tuple[int, int, int]] = "white",
        highlight_color: Union[str, Tuple[int, int, int], None] = None,
    ) -> None: ...
    @property
    def text(self) -> str: ...
    @property
    def position(self) -> Tuple[int, int]: ...
    @property
    def font(self) -> Union[PIL.ImageFont.FreeTypeFont, PIL.ImageFont.ImageFont]: ...
    @property
    def color(self) -> Union[str, Tuple[int, int, int]]: ...
    @property
    def highlight_color(self) -> Union[str, Tuple[int, int, int]]: ...
    def render(self, draw: PIL.ImageDraw.ImageDraw) -> None: ...
