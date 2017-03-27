from collections import ChainMap
from flocs.context import dynamic
from flocs.store import Store
from flocs.state import State, default_entities
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

db_entities = ChainMap({
  entity_class: DbEntityMap.for_model(model)
  for (entity_class, model) in model_mapping.items()
}, default_entities)

db_state = State(entities=db_entities).add_context(dynamic)


class PersistenceHooks(Store.Hooks):
    def __init__(self, request_context):
        self.request_context = request_context

    def post_commit(self, state, diff):
        for entity_name, entity_id, entity in diff:
            model_mapping[entity_name].import_entity(entity=entity, **self.request_context)


def open_django_store(request=None):
    """ Return store as a context manager

    You can set additional attributes from request context, such as user, to be
    considered by store.
    """
    request_context = {}
    if request is not None:
        request_context['user'] = request.user
    persistence_hooks = PersistenceHooks(request_context=request_context)
    store_context_manager = Store.open(state=db_state, hooks=persistence_hooks)
    return store_context_manager
