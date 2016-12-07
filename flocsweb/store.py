from collections import ChainMap, MutableMapping
from flocs.store import Store
from practice.models import Student as StudentModel, TaskInstance as TaskInstanceModel
from flocs.state import STATIC_ENTITIES
from flocs.entities import Student
from flocs.entities import TaskSession as TaskInstance


class LazyDatabaseDict(MutableMapping):
    def __init__(self, model=None, *args, **kwargs):
        self.store = dict()
        self.model = model
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def get(self, key, default=None):
        if key not in self.store:
            try:
                self.store[key] = self.model.objects.get(pk=key).to_named_tuple()
            except self.model.DoesNotExist:
                self.store[key] = None
        entity = self.store[key]
        return entity if entity else default

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)


entity_model_mapping = {
    Student: StudentModel,
    TaskInstance: TaskInstanceModel,
}


class PersistenceHooks(Store.Hooks):
    def __init__(self, request_context):
        self.request_context = request_context

    def post_commit(self, state, diff, actions):
        for entity_name, entity_id, entity in diff:
            entity_model_mapping[entity_name].from_named_tuple(entity_tuple=entity, **self.request_context).save()


def get_all_entities():
    dynamic_entities = {entity: LazyDatabaseDict(model) for (entity, model) in entity_model_mapping.items()}
    return ChainMap(dynamic_entities, STATIC_ENTITIES)


def open_django_store(request_context={}):
    return Store.open(get_all_entities(), hooks=PersistenceHooks(request_context))
