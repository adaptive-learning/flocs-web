from collections import ChainMap
from flocs.context import dynamic
from flocs.store import Store
from flocs.state import State, default
from flocs import entities
from users.services import get_or_create_user
import practice.models
from flocsweb.models import Action
from .db_entity_map import DbEntityMap


model_mapping = {
    entities.Student: practice.models.Student,
    entities.Session: practice.models.Session,
    entities.TaskSession: practice.models.TaskSession,
    entities.ProgramSnapshot: practice.models.ProgramSnapshot,
    entities.SeenInstruction: practice.models.SeenInstruction,
    entities.Action: Action,
}

db_entities = ChainMap({
    entity_class: DbEntityMap.for_model(model)
    for (entity_class, model) in model_mapping.items()
}, default.entities)

db_state = State(entities=db_entities).add_context(dynamic)


class PersistenceHooks(Store.Hooks):
    def __init__(self, request_context):
        self.request_context = request_context

    def post_commit(self, state, diff):
        # enforce correct order of entities to avoid integrity constraint violations
        order = [
            entities.Student,
            entities.Session,
            entities.TaskSession,
            entities.ProgramSnapshot,
            entities.SeenInstruction,
            entities.Action,
        ]
        sorted_diff = sorted(diff, key=lambda d: order.index(d[0]))
        for entity_class, _entity_id, entity in sorted_diff:
            model_mapping[entity_class].import_entity(entity=entity, **self.request_context)


def open_django_store(request=None):
    """ Return store as a context manager

    You can set additional attributes from request context, such as user, to be
    considered by store.
    """
    request_context = {}
    if request is not None:
        request_context['user'] = get_or_create_user(request)
    persistence_hooks = PersistenceHooks(request_context=request_context)
    store_context_manager = Store.open(state=db_state, hooks=persistence_hooks)
    return store_context_manager
