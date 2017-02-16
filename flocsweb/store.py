from collections import ChainMap
from flocs.store import Store
from flocs.state import STATIC_ENTITIES   # TODO: remove this import
from flocs import entities
import practice.models
from .db_entity_map import DbEntityMap


model_mapping = {
    entities.Student: practice.models.Student,
    entities.TaskSession: practice.models.TaskSession,
}


class PersistenceHooks(Store.Hooks):
    def __init__(self, request_context):
        self.request_context = request_context

    def post_commit(self, state, diff, actions):
        for entity_name, entity_id, entity in diff:
            model_mapping[entity_name].from_named_tuple(entity_tuple=entity, **self.request_context).save()


def get_all_entities():
    dynamic_entities = {
        entity: DbEntityMap.for_model(model)
        for (entity, model) in model_mapping.items()}
    return ChainMap(dynamic_entities, STATIC_ENTITIES)


# TODO: fix request_context={} -> use None instead and resolve in body
def open_django_store(request_context={}):
    return Store.open(get_all_entities(), hooks=PersistenceHooks(request_context))
