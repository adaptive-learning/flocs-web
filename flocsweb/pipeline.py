from django.contrib.auth import login, logout
from lazysignup.utils import is_lazy_user
from users.services import delete_lazy_user


def remove_current_user(backend, uid, user=None, *args, **kwargs):
    """
    Handles cases where there was a user logged in (or lazy user) when the
    social authentication started. Normal users are logged out. Lazy users are
    kept, if and only if social account has not yet been used.
    """
    extra_login = False
    request = backend.strategy.request
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    session_next = backend.strategy.session_get('next')

    if social:
        if user and social.user != user:
            if is_lazy_user(user):
                user.delete()
            else:
                logout(request)
            user = None
            extra_login = True
    else:
        if user and is_lazy_user(user):
                delete_lazy_user(user)

    if session_next:
        backend.strategy.session_set('next', session_next)
    return {'user': user, 'extra_login': extra_login, 'backend': backend}


def force_login(backend, user=None, extra_login=False, *args, **kwargs):
    """
    Due to custom behaviour regarding user already present in time of social
    login, this function will force log in of the social user if required.
    """
    if extra_login:
        # backed is especially needed in cases where lazy users are converted
        # to social ones, otherwise they are still treated as lazy
        user.backend = '{0}.{1}'.format(backend.__module__,
                                        backend.__class__.__name__)
        login(backend.strategy.request, user)
    return None
