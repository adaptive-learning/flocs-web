from core.data.fixtures.toolboxes import TOOLBOXES


class ToolboxManager(object):
    IMPLIED_BLOCKS_IDENTIFIERS = ['start', 'math_number']

    @staticmethod
    def get_initial_toolbox():
        # toolboxes are ordered by their level
        assert TOOLBOXES, 'There are no toolboxes available!'
        return TOOLBOXES[0]

    @staticmethod
    def get_complete_toolbox():
        assert TOOLBOXES, 'There are no toolboxes available!'
        return TOOLBOXES[-1]

    @staticmethod
    def get_first_toolbox_containing(blocks):
        """ Return toolbox with lowest level which contains given blocks
        """
        # disregard blocks which appear in workspace implicitly
        blocks = {block for block in blocks
                  if block and block.identifier not in ToolboxManager.IMPLIED_BLOCKS_IDENTIFIERS}
        for toolbox in TOOLBOXES:
            if blocks.issubset(toolbox.get_all_blocks()):
                return toolbox
        raise ValueError('No toolbox containing all blocks.')

    @staticmethod
    def get_next(toolbox):
        """ Return the toolbox which follows the given toolbox.
            Return None, if there is no more advanced toolbox available.
        """
        # toolboxes are ordered by their level and indexed from 0
        return TOOLBOXES[toolbox.level] if len(TOOLBOXES) >= toolbox.level else None

    @staticmethod
    def get_prev(toolbox):
        """ Return the toolbox which precedes the given toolbox.
            Return None, if there is no preceding toolbox.
        """
        return TOOLBOXES[toolbox.level - 2] if toolbox.level > 1 else None

    @staticmethod
    def get_by_natural_key(name):
        match = [toolbox for toolbox in TOOLBOXES if toolbox.name == name]
        assert len(match) <= 1, 'Multiple matches for the same toolbox name!'
        return match[0] if match else None

    @staticmethod
    def get_by_attribute(attribute, value):
        match = [toolbox for toolbox in TOOLBOXES if toolbox.__dict__.get(attribute) == value]
        if len(match) > 1:
            raise ValueError('Multiple matches for the same toolbox name!')
        return match[0] if match else None

    @staticmethod
    def as_db_type():
        return [(obj.pk, obj.name) for obj in TOOLBOXES]

    @staticmethod
    def from_db_type(pk):
        return ToolboxManager.get_by_attribute('pk', pk)
