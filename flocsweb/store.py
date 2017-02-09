from collections import ChainMap, Mapping
from practice.models import Student as StudentModel, TaskSession as TaskSessionModel
from flocs.store import Store
from flocs.state import STATIC_ENTITIES, EntityMapping
from flocs.entities import Student
from flocs.entities import TaskSession


class DbEntityMapping(Mapping):
    """Collection of all entities of given type, lazily loaded from DB
    """
    model_mapping = {
        Student: StudentModel,
        TaskSession: TaskSessionModel,
    }


    #@classmethod
    #def from_list(cls, entity_list):
    #    return cls({get_id(entity): entity for entity in entity_list})

    def __init__(self, data=None, model=None, manager=None):
        assert data or model
        self.data = data or {}
        self.model = model or self.model_mapping[list(data.values())[0].__class__]
        self.manager = manager or self.model.objects

    @classmethod
    def from_list(cls, entity_list):
        # just return entity list, TODO: unhack (using self.manager?)
        return EntityMapping.from_list(entity_list)
        ## TODO: if entity_list empty
        #entity = entity_list[0]
        #print(entity, type(entity))
        #model = cls.model_mapping[entity.__class__]
        #db_entities = [model.from_named_tuple(entity) for entity in entity_list]
        #print('entities', db_entities)
        #data = {db_entity.pk: db_entity for db_entity in db_entities}
        #return cls(model=model, data=data)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __getitem__(self, key):
        if key not in self.data:
            try:
                self.data[key] = self.manager.get(pk=key).to_named_tuple()
            except self.model.DoesNotExist as exc:
                raise KeyError(str(exc))
        entity = self.data[key]
        return entity

    def __iter__(self):
        print('model is', self.model)
        for entity in self.manager.all():
            yield entity.pk

    def __len__(self):
        return self.manager.count()

    def __eq__(self, other):
        print('eq')
        print(self.to_dict(), other.to_dict())
        return self.to_dict() == other.to_dict()

    def filter(self, **kwargs):
        return DbEntityMapping(model=self.model, manager=self.manager.filter(**kwargs))

    def to_dict(self):
        return {key: self[key] for key in iter(self)}


class PersistenceHooks(Store.Hooks):
    def __init__(self, request_context):
        self.request_context = request_context

    def post_commit(self, state, diff, actions):
        for entity_name, entity_id, entity in diff:
            DbEntityMapping.model_mapping[entity_name].from_named_tuple(entity_tuple=entity, **self.request_context).save()


def get_all_entities():
    dynamic_entities = {entity: DbEntityMapping(model=model) for (entity, model) in DbEntityMapping.model_mapping.items()}
    return ChainMap(dynamic_entities, STATIC_ENTITIES)


def open_django_store(request_context={}):
    return Store.open(get_all_entities(), hooks=PersistenceHooks(request_context))
