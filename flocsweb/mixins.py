from collections import namedtuple


class ExportMixin(object):
    """
    A mixin class providing import and export features using named tuples. If a class has a specific named tuple it
    wants to be exported to it should override named_tuple attribute.
    """
    named_tuple = None

    def to_named_tuple(self):
        """
        Exports selected attributes to named tuple. Selection depends on the attribute named_tuple
        Returns: named tuple with attribute values
        """
        named_tuple = self.named_tuple if self.named_tuple else namedtuple(self.__class__.__name__, self.__dict__)
        return named_tuple(**{k: get_field(self, k) for k in named_tuple._fields})


def get_field(db_entity, entity_field_name):
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
