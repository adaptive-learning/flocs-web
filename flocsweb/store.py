from collections import ChainMap
from flocs.store import Store
from flocs.state import STATIC_ENTITIES   # TODO: remove this import
from flocs import entities
from flocsweb.models import Action
import practice.models
from .db_entity_map import DbEntityMap


model_mapping = {
    entities.Student: practice.models.Student,
    entities.TaskSession: practice.models.TaskSession,
    entities.SeenInstruction: practice.models.SeenInstruction,
    entities.Action: Action,
}


class PersistenceHooks(Store.Hooks):
    def __init__(self, request_context):
        self.request_context = request_context

    def post_commit(self, state, diff):
        for entity_name, entity_id, entity in diff:
            model_mapping[entity_name].import_entity(entity=entity, **self.request_context)


def get_all_entities():
    dynamic_entities = {
        entity: DbEntityMap.for_model(model)
        for (entity, model) in model_mapping.items()}
    return ChainMap(dynamic_entities, STATIC_ENTITIES)


def open_django_store(**request_context):
    """ Return store as a context manager

    You can set additional attributes from request context, such as user, to be
    considered by store.
    """
    request_context = request_context or {}
    persistence_hooks = PersistenceHooks(request_context)
    store_context_manager = Store.open(entities=get_all_entities(), hooks=persistence_hooks)
    return store_context_manager
