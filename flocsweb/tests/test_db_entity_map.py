from django.conf import settings
import pytest
from flocs.tests.test_entity_map import TestEntityMap, e1, e2
from flocsweb.store import DbEntityMap
from flocsweb.tests.models import DbEntity


@pytest.mark.django_db
class TestDbEntityMap(TestEntityMap):
    """ Tests from core to ensure expected behavior of DbEntityMap

    Perform all tests from TestEntityMap plus a few additional
    """

    @staticmethod
    def create_entity_map(*entities):
        for entity in entities:
            DbEntity.import_entity(entity)
        query_set = DbEntity.objects.filter(pk__in=[e.entity_id for e in entities])
        return DbEntityMap(query_set=query_set)

    def test_set_puts_db_at_the_end(self):
        initial_entity_map = self.create_entity_map(e1)
        updated_entity_map = initial_entity_map.set(e2)
        last_map = updated_entity_map.chain_map.maps[1]
        assert isinstance(last_map, DbEntityMap)
