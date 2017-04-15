from warnings import warn
from collections.abc import Mapping
from flocs.state import EntityMap

class DbEntityMap(Mapping):
    """ DB facade/adapter for a single relation (Django's QuerySet)
        providing flocs.EntityMap interface
    """

    def __init__(self, query_set=None):
        self.query_set = query_set

    @classmethod
    def for_model(cls, model):
        query_set = model.objects.all()
        return cls(query_set)

    @classmethod
    def from_list(cls, entity_list):
        # TODO: this could be implemented similarly as create_entity_map in
        # test_db_entity_map, but maybe we don't need it for anything
        raise NotImplementedError()

    def __getitem__(self, entity_id):
        try:
            db_entity = self.query_set.get(pk=entity_id)
            entity = db_entity.to_namedtuple()
            return entity
        except self.model_class.DoesNotExist as exc:
            raise KeyError(str(exc))

    def __iter__(self):
        if (len(self) > 500):
            # TODO: use logging?
            warn('Iterating through a long query set of {model} ({count} items)'
                .format(model=self.model_class, count=len(self)))
        for db_entity in self.query_set:
            yield db_entity.pk

    def __contains__(self, entity_id):
        return self.query_set.filter(pk=entity_id).exists()

    def __len__(self):
        return self.query_set.count()

    def __repr__(self):
        return 'DbEntityMap({query_set})'.format(query_set=self.query_set)

    @property
    def model_class(self):
        return self.query_set.model

    @property
    def entity_class(self):
        return self.model_class.entity_class

    def set(self, entity):
        """ Return a new EntityMap from self and the given entity
        """
        return EntityMap(self).set(entity)

    @property
    def original_entities(self):
        # if something changed we would have created EntityMap
        return self

    @property
    def modified_entities(self):
        # if something changed we would have created EntityMap
        return {}

    def filter(self, **kwargs):
        return DbEntityMap(query_set=self.query_set.filter(**kwargs))

    def order_by(self, *fields):
        return DbEntityMap(query_set=self.query_set.order_by(*fields))

    def first(self):
        db_entity = self.query_set.first()
        return  db_entity.to_namedtuple() if db_entity else None

    def last(self):
        db_entity = self.query_set.last()
        return  db_entity.to_namedtuple() if db_entity else None

    def exists(self):
        return self.query_set.exists()
