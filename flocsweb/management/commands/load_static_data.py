from django.core.management.base import BaseCommand
from flocs.data import TASKS
from tasks.models import Task


class Command(BaseCommand):
    help = "Loads static data into the database, if it has not been done yet."

    def handle(self, *args, **options):
        for task_tuple in TASKS:
            if not Task.objects.filter(**task_tuple._asdict()):
                Task.from_named_tuple(task_tuple).save()
                self.stdout.write(task_tuple.__str__() + " has been loaded.")
