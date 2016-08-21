from rest_framework import viewsets
from rest_framework.exceptions import NotFound


class ReadOnlyNonModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A class for providing list and retrieve methods for non model (fixture)
    objects.

    Set fixtures property to a list of your fixtures.
    """
    fixtures = []

    def get_queryset(self):
        return self.fixtures

    def get_object(self):
        # lookup_field defaults to 'pk'
        lookup_value = self.kwargs[self.lookup_field]
        match = [obj for obj in self.fixtures if str(obj.__dict__[self.lookup_field]) == lookup_value]
        assert len(match) <= 1, 'There are multiple object with the same lookup value'
        if match:
            return match[0]
        else:
            raise NotFound
