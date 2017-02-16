from collections.abc import Mapping
from flocs.state import EntityMap

class DbEntityMap(Mapping):
    """ DB facade/adapter for a single relation (Django's QuerySet)
        providing flocs.EntityMap interface
    """

    def __init__(self, querySet=None):
        self.querySet = querySet

    @classmethod
    def for_model(cls, model):
        querySet = model.objects.all()
        return cls(querySet)

    @classmethod
    def from_list(cls, entity_list):
        # TODO: this could be implemented similarly as create_entity_map in
        # test_db_entity_map, but maybe we don't need it for anything
        raise NotImplementedError()

    def __getitem__(self, entity_id):
        try:
            entity = self.querySet.get(pk=entity_id).to_named_tuple()
            return entity
        except self.model_class.DoesNotExist as exc:
            raise KeyError(str(exc))

    def __iter__(self):
        for db_entity in self.querySet:
            yield db_entity.pk

    def __len__(self):
        return self.querySet.count()

    def __repr__(self):
        return 'DbEntityMapping({querySet})'.format(querySet=self.querySet)

    @property
    def model_class(self):
        return self.querySet.model

    @property
    def entity_class(self):
        return self.model_class.named_tuple

    def set(self, entity):
        ''' Return a new EntityMap from self and the given entity
        '''
        return EntityMap(self).set(entity)

    def filter(self, **kwargs):
        return DbEntityMap(querySet=self.querySet.filter(**kwargs))
