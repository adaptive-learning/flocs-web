class Toolbox(object):
    """ Model for a collection of blocks with associated level and credit value
    """

    def __init__(self, pk, name, blocks, level=1, credits=0):
        self.pk = pk
        self.name = name
        self.blocks = blocks
        self.level = level
        self.credits = credits

    def natural_key(self):
        return (self.name,)

    def get_new_blocks(self):
        current_blocks = set(self.get_all_blocks())
        prev_toolbox = Toolbox.objects.get_prev(self)
        old_blocks = set(prev_toolbox.get_all_blocks()) if prev_toolbox else set()
        new_blocks = current_blocks - old_blocks
        return list(new_blocks)

    def get_all_blocks(self):
        return self.blocks

    def __str__(self):
        return '[{level}] {name}'.format(
            level=self.level,
            name=self.name)
