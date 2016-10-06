from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound


@api_view()
def wrong_api_call(request):
    """
    Handles non-existent API calls (404 error).
    """
    raise NotFound(detail='Wrong api call.')


def redirect_home(request):
    """
    Redirect to home path URL
    """
    return redirect('/')


@ensure_csrf_cookie
def frontend_app(request, *_):
    return render(request, 'index.html')
