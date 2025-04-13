# pylint: disable=all

from typing import Tuple, Union

from ..argval import enforce_type
from ..supers import FXNode

class Canvas:
    def __init__(
        self,
        root: FXNode,
        size: Tuple[int, int] = (1280, 720),
        bg_color: Union[str, Tuple[int, int, int]] = "black",
    ) -> None: ...
    @property
    def root(self) -> FXNode: ...
    @property
    def size(self) -> Tuple[int, int]: ...
    @property
    def bg_color(self) -> Union[str, Tuple[int, int, int]]: ...
