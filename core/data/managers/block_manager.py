from core.data.fixtures.blocks import BLOCKS


class BlockManager(object):
    @staticmethod
    def get_by_natural_key(identifier):
        match = [block for block in BLOCKS if block.identifier == identifier]
        assert len(match) <= 1, 'Multiple matches for the same block name!'
        return match[0] if match else None
