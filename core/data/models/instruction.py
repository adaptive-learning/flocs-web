"""
Model for instruction that is shown to user in case he deals with new (or not
yet mastered) concept.
"""
from collections import namedtuple


class Instruction(object):
    """ Instruction for better understanding of a specific concept by
        a student. Each instruction belongs to certain concept.
    """

    def __init__(self, pk, concept, text, order=0):
        self.pk = pk
        self.concept = concept
        self.text = text
        self.order = order

    export_class = namedtuple('Instruction',
                              ['instruction_id', 'concept_id', 'order', 'text'])

    def to_export_tuple(self):
        export_tuple = self.export_class(
            instruction_id=self.pk,
            concept_id=self.concept.pk,
            order=self.order,
            text=self.text)
        return export_tuple

    def __str__(self):
        templ = 'concept={concept}, text={text}'
        return templ.format(concept=self.concept, text=self.text)
