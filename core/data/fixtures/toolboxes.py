from core.data.models.toolbox import Toolbox
from .blocks import BLOCKS

TOOLBOXES = [
    Toolbox(pk=1, name='forward', level=1, credits=1, blocks=BLOCKS[:1]),
    Toolbox(pk=2, name='movement', level=2, credits=1, blocks=BLOCKS[:2])
]