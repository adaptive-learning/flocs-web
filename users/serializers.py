from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from lazysignup.utils import is_lazy_user
from social.apps.django_app.default.models import UserSocialAuth
from users.services import create_or_convert


class IsSocialUserField(serializers.Field):
    """
    Requires whole user to be passed (source=*)
    """

    def to_representation(self, obj):
        return UserSocialAuth.objects.filter(user=obj) or False


class IsLazyUserField(serializers.Field):
    """
    Requires whole user to be passed (source=*)
    """

    def to_representation(self, obj):
        return is_lazy_user(obj)


class ProvidersField(serializers.Field):
    """
    Requires whole user to be passed (source=*)
    """

    def to_representation(self, obj):
        return [social_user.provider for social_user in UserSocialAuth.objects.filter(user=obj)]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.IntegerField(read_only=True, source='id')
    username = serializers.RegexField(
        regex=r'[\w@+.-]*',
        max_length=30,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    is_lazy_user = IsLazyUserField(read_only=True, source='*')
    is_social_user = IsSocialUserField(read_only=True, source='*')
    providers = ProvidersField(read_only=True, source='*')

    class Meta:
        model = User
        fields = ('url', 'user_id', 'username', 'password', 'email', 'first_name', 'is_staff', 'is_authenticated',
                  'is_lazy_user', 'is_social_user', 'providers')
        read_only_fields = ('is_staff', 'user_id', 'is_authenticated')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'max_length': 30, 'required': False},
        }

    def create(self, validated_data):
        """
        Custom implementation of user creation due to lazy users.
        """
        return create_or_convert(
            user=self.context['request'].user,
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            password=validated_data['password']
        )
