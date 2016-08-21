from core.data.models.instruction import Instruction
from .concepts import BLOCK_MOVE

INSTRUCTIONS = [
    Instruction(pk=1, concept=BLOCK_MOVE,
                text="Tento příkaz říká robotovi, aby popojel o jedno políčko ve směru, kterým se dívá.", order=135)
]