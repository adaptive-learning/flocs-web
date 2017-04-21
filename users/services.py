from lazysignup.decorators import allow_lazy_user
from lazysignup.utils import is_lazy_user
from lazysignup.models import LazyUser
from lazysignup.signals import converted
from django.contrib.auth.models import User
from django.contrib.auth import login as djangologin, logout as djangologout
from django.contrib.auth import authenticate


@allow_lazy_user
def get_or_create_user(request):
    """ Return a current user and create one if it doesn't exist
    """
    return request.user


def create_or_convert(user, email, first_name, password):
    """
    Creates a new user unless the current user is lazy one. In that case the
    lazy user is converted and user details are updated.
    """
    # usernames do not allow whole range of characters, so we generate them from email
    username = email
    if user and is_lazy_user(user):
        user.username = username
        user.email = email
        user.first_name = first_name
    else:
        user = User(
            username=username,
            email=email,
            first_name=first_name
        )
    user.set_password(password)
    return delete_lazy_user(user)


def delete_lazy_user(user):
    """
    If there is a lazy user associated with the given user, it is deleted.
    """
    qs = LazyUser.objects.filter(user=user)
    if qs:
        qs.delete()
        LazyUser.objects.update()
        converted.send(None, user=user)
    # set default authentication backend
    user.backend = None
    user.save()
    assert not is_lazy_user(user)
    return user


def login(request, username, password):
    user = authenticate(username=username, password=password)
    # TODO: properly handle these scenarios
    if user is None or not user.is_active:
        return None

    # TODO: Throws away any progress made before login, this should probably
    # not happen. Also seems to throw some exceptions.
    if is_lazy_user(request.user):
        LazyUser.objects.filter(user=request.user).delete()
        request.user.delete()
    djangologin(request, user)
    return user


def logout(request):
    djangologout(request)
