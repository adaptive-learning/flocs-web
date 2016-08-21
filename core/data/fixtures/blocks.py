from core.data.models.block import Block

MAZE_MOVE_FORWARD = Block(pk=1, identifier='maze_move_forward', name='Krok vpřed')
MAZE_TURN = Block(pk=2, identifier='maze_turn', name='Zatoč',
                  expanded_identifiers='["maze_turn_left", "maze_turn_right"]')

BLOCKS = [
    MAZE_MOVE_FORWARD,
    MAZE_TURN
]
