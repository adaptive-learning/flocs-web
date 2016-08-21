from core.data.fixtures.concepts import CONCEPTS


class ConceptManager(object):
    @staticmethod
    def get_by_natural_key(name):
        match = [concept for concept in CONCEPTS if concept.name == name]
        assert len(match) <= 1, 'Multiple matches for the same concept name!'
        return match[0] if match else None

    @staticmethod
    def as_db_type():
        return [(str(obj.pk), obj.name) for obj in CONCEPTS]

    @staticmethod
    def from_db_type(choices):
        return [obj for obj in CONCEPTS if str(obj.pk) in choices]
