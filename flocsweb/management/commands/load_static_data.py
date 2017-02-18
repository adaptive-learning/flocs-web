from django.core.management.base import BaseCommand
from flocs.data import tasks
from tasks.models import Task


class Command(BaseCommand):
    help = "Loads static data into the database, if it has not been done yet."

    def handle(self, *args, **options):
        self.stdout.write('----------------------------')
        self.stdout.write('Loading tasks')
        self.stdout.write('----------------------------')
        for task_tuple in tasks:
            task = Task.from_named_tuple(task_tuple)
            task.save()
            self.stdout.write('Loaded task: {task}'.format(task=task))
        self.stdout.write('----------------------------')
        self.stdout.write('Loaded {n} tasks'.format(n=len(tasks)))
        self.stdout.write('----------------------------')
