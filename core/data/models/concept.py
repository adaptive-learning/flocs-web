from collections import namedtuple

TYPES = ['environment', 'game', 'block', 'programming']


class ConceptMixin(object):
    """ Mixin with common concept interface. Requires classes to override pk,
        name, and type attributes.
        A feature of students and tasks which influence the solving process.
        Concepts of a student determine her skill.
        Concepts of a task determine its difficulty.
    """
    export_class = namedtuple('Concept', ['concept_id', 'name', 'type'])
    pk = None
    name = None
    type = None

    def to_export_tuple(self):
        export_tuple = self.export_class(
            concept_id=self.pk,
            name=self.name,
            type=self.type)
        return export_tuple

    def __str__(self):
        return '[{pk}] {name}'.format(pk=self.pk, name=self.name)


class ProgrammingConcept(ConceptMixin):
    """ Concept of a certain programming skill, such as usage of commands,
        loops, conditions or functions.
    """

    def __init__(self, pk, name, subconcepts):
        self.pk = pk
        self.name = name
        self.type = 'programming'
        self.subconcepts = subconcepts


class BlockConcept(ConceptMixin):
    """ Concept of a single command block.
        A student either know or doesn't know what the block does.
        A task either require the block for the solution or not.
    """

    def __init__(self, pk, name, block):
        self.pk = pk
        self.name = name
        self.type = 'block'
        self.block = block


class GameConcept(ConceptMixin):
    """ Concept describing some aspect of problem setting (e.g. tokens).
        A student is either familiar with this aspect or is not.
        A task either contains this aspect or does not .
    """

    def __init__(self, pk, name, checker=None):
        self.pk = pk
        self.name = name
        self.type = 'game'
        self.checker = checker

    def is_contained_in(self, task):
        if not self.checker:
            return False
        concept_presence_checker = getattr(task, self.checker)
        return concept_presence_checker()


class EnvironmentConcept(ConceptMixin):
    """ Concept describing some aspect of the system environment
        A student is either familiar with this aspect or is not.
        Currently, all tasks contain all environment aspects.
    """

    def __init__(self, pk, name):
        self.pk = pk
        self.name = name
        self.type = 'environment'
