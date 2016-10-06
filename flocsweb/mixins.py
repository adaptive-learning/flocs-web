from collections import namedtuple


class ExportMixin(object):
    """
    A mixin class providing import and export features using named tuples. If a class has a specific named tuple it
    wants to be exported to it should override named_tuple attribute.
    """
    named_tuple = None

    def to_named_tuple(self):
        """
        Exports selected attributes to named tuple. Selection depends on the attribute named_tuple
        Returns: named tuple with attribute values
        """
        named_tuple = self.named_tuple if self.named_tuple else namedtuple(self.__class__.__name__, self.__dict__)
        return named_tuple(**{k: self.__dict__[k] for k in named_tuple._fields})
