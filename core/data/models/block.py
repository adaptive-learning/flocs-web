""" DB model for a command block, e.g. "Move forward" or "Repeat N-times"
"""
import json
from collections import namedtuple


class Block(object):
    """Representation of a code block
    """

    def __init__(self, pk, name, identifier, expanded_identifiers=None):
        self.pk = pk
        self.name = name
        self.identifier = identifier
        self._expanded_identifiers = expanded_identifiers

    export_class = namedtuple('Block', ['block_id', 'identifier', 'name'])

    def natural_key(self):
        return (self.identifier,)

    def get_identifiers_expanded_list(self):
        if not self._expanded_identifiers:
            return [self.identifier]
        return json.loads(self._expanded_identifiers)

    def __str__(self):
        return '[{pk}] {name}'.format(pk=self.pk, name=self.name)

    def to_export_tuple(self):
        export_tuple = self.export_class(
            block_id=self.pk,
            identifier=self.identifier,
            name=self.name)
        return export_tuple

    def to_json(self):
        """Returns JSON (dictionary) representation of the block.
        """
        block_dict = {
            'block-id': self.pk,
            'name': self.name,
            'identifier': self.identifier,
            'identifiers-expanded': self.get_identifiers_expanded_list()
        }
        return block_dict
