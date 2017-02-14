from django.conf import settings
import pytest
from flocs.tests.test_state import TestEntityMapping
from flocsweb.store import DbEntityMapping
from flocsweb.tests.models import Entity

@pytest.mark.django_db
class TestDbEntityMapping(TestEntityMapping):
    """ Tests from core to ensure expected behavior of DbEntityMapping
    """
    entity_mapping_class = DbEntityMapping

    @pytest.fixture(autouse=True)
    def setup_method_db(self, db):
        # TODO: dry (same data as in core tests)
        Entity.objects.create(entity_id='i', a=1, b=1)
        Entity.objects.create(entity_id='j', a=2, b=1)
        Entity.objects.create(entity_id='k', a=1, b=2)
        original_model_mapping = DbEntityMapping.model_mapping
        DbEntityMapping.model_mapping = {
            TestEntityMapping.entity_class: Entity,
        }
        self.entity_mapping = DbEntityMapping(model=Entity)
        yield
        DbEntityMapping.model_mapping = original_model_mapping
