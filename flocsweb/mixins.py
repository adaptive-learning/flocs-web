from collections import namedtuple
from django.apps import apps


class ImportExportMixin(object):
    """ Provides import and export from and to a plain entity (named tuple)

    Each class inheriting ImportExportMixin must define corresponding entity
    class as a class-level attribute. The entity class must be a namedtuple, or
    any class providing complete initializer and _asdict method.

    For each field of the entity class, Django model must implement
    corresponding field (or computed property) of corresponding name:

    Entity x ---> db_entity x
    1) x_id  ---> primary key x_id
    2) y     ---> atomic field y (number, string, etc.)
    3) z_id  ---> 1:1 or 1:m relationship to model z with name z
    4) z_ids ---> m:n relationship to model z with name zs (note the "s" suffix)
    """
    entity_class = None

    def to_namedtuple(self):
        """ Return a plain entity with fields specified by self.entity_class
        """
        assert callable(self.entity_class)
        field_names = self.entity_class._fields
        field_value_map = {field_name: get_field(self, field_name) for field_name in field_names}
        return self.entity_class(**field_value_map)  # pylint:disable=not-callable

    @classmethod
    def import_entity(cls, entity, *args, **kwargs):
        """ Create a db entity from given entity and store it in DB
        If the entity is already present in DB, it will be updated.

        Args:
            entity: namedtuple with _asdict method

        Returns:
            created or updated DB entity
        """
        attributes = entity._asdict()
        ids_attribute_names = [name for name in attributes if name.endswith('_ids')]
        for ids_attribute_name in ids_attribute_names:
            del attributes[ids_attribute_name]
        db_entity = cls(**attributes)
        db_entity.save()
        for ids_attribute_name in ids_attribute_names:
            related_entity_ids = getattr(entity, ids_attribute_name)
            db_attribute_name = ids_attribute_name[:-4] + 's'
            relationship = getattr(db_entity, db_attribute_name)
            related_model = relationship.model
            related_db_entities = related_model.objects.filter(pk__in=related_entity_ids)
            relationship.add(*related_db_entities)
        return db_entity


def get_field(db_entity, entity_field_name):
    """ Get value of given field of given entity

    Note that Django automatically adds z_id field for each foreign key z, so
    1:1 and 1:m relationships are handled in the same way as atomic values.
    """
    if entity_field_name in db_entity.__dict__:
        return db_entity.__dict__[entity_field_name]
    if entity_field_name.endswith('_ids'):
        return get_many_to_many_field(db_entity, entity_field_name)
    return get_property_field(db_entity, entity_field_name)


def get_property_field(db_entity, entity_field_name):
    # some fields are properties and therefore in class __dict__ and not object __dict__
    return db_entity.__class__.__dict__[entity_field_name].fget(db_entity)

def get_many_to_many_field(db_entity, entity_field_name):
    assert entity_field_name.endswith('_ids')
    attribute_name = entity_field_name[:-4] + 's'
    related_db_entity_id_attribute_name = entity_field_name[:-1]
    related_db_entities_manager = db_entity.__getattribute__(attribute_name)
    related_entity_ids = related_db_entities_manager.values_list(related_db_entity_id_attribute_name, flat=True)
    return related_entity_ids
