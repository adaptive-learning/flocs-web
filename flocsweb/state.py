from datetime import datetime
from sys import maxsize
from random import random
from practice.models import Student, TaskInstance
from flocs.state import State, LazyValue


def create_django_state():
    state = State({
        'entities.students': LazyValue(list(map(lambda i: i.to_named_tuple(), Student.objects.all()))),
        'entities.task_instances': LazyValue(list(map(lambda i: i.to_named_tuple(), TaskInstance.objects.all()))),
        'context.time': datetime.now(),
        'context.randomness_seed': random.randint(0, maxsize)
    })
    return state
