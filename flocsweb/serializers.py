from rest_framework import serializers
from .models import Action
from .store import open_django_store


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    action_id = serializers.ReadOnlyField()
    class Meta:
        model = Action
        read_only_fields = ('randomness', 'version')

    def create(self, validated_data):
        """ Create a new action (if not already stored) and return it
        """
        if 'action_id' in validated_data:
            action, created = Action.objects.get_or_create(
                action_id=validated_data['action_id'],
                defaults=validated_data,
            )
            return action
        return Action.create(**validated_data)
