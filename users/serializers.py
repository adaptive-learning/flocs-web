from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from lazysignup.utils import is_lazy_user
from social.apps.django_app.default.models import UserSocialAuth
from users.services import create_or_convert


class StringListField(serializers.ListField):
    child = serializers.CharField()


class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    username = serializers.RegexField(
        regex=r'[\w@+.-]*',
        max_length=30,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False, max_length=30)
    is_staff = serializers.BooleanField(read_only=True)
    is_authenticated = serializers.BooleanField(read_only=True)
    is_lazy_user = serializers.BooleanField(read_only=True)
    is_social = serializers.BooleanField(read_only=True)
    providers = StringListField(read_only=True)

    # custom mapping of fields to object "properties"
    def to_representation(self, obj):
        qs = UserSocialAuth.objects.filter(user=obj)
        return {
            'id': obj.pk,
            'username': obj.username,
            'email': obj.email,
            'first_name': obj.first_name,
            'is_staff': obj.is_staff,
            'is_authenticated': obj.is_authenticated(),
            'is_lazy_user': is_lazy_user(obj),
            'is_social': qs or False,
            'providers': [social_user.provider for social_user in qs]
        }

    def create(self, validated_data):
        return create_or_convert(
            user=self.context['request'].user,
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            password=validated_data['password']
        )

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
