from datetime import datetime
from sys import maxsize
from random import random
from practice.models import Student, TaskSession
from flocs.state import State, LazyValue


def create_django_state():
    state = State({
        'entities.students': LazyValue(list(map(lambda i: i.to_named_tuple(), Student.objects.all()))),
        'entities.task_sessions': LazyValue(list(map(lambda i: i.to_named_tuple(), TaskSession.objects.all()))),
        'context.time': datetime.now(),
        'context.randomness_seed': random.randint(0, maxsize)
    })
    return state
