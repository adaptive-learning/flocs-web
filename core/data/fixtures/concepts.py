from core.data.models.concept import BlockConcept, ProgrammingConcept, EnvironmentConcept, GameConcept
from .blocks import MAZE_MOVE_FORWARD, MAZE_TURN

BLOCK_MOVE = BlockConcept(pk=1, name='BLOCK_MOVE', block=MAZE_MOVE_FORWARD)
BLOCK_TURN = BlockConcept(pk=2, name='BLOCK_TURN', block=MAZE_TURN)

CONCEPTS = [
    BLOCK_MOVE,
    BLOCK_TURN,
    ProgrammingConcept(pk=20, name='PROGRAMMING_SEQUENCE', subconcepts={BLOCK_MOVE, BLOCK_MOVE}),
    EnvironmentConcept(pk=11, name='ENV_MAZE'),
    GameConcept(pk=17, name='GAME_COLORS', checker='contains_colors')
]