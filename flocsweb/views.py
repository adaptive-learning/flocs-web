from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound


@api_view()
def wrong_api_call(request):
    """
    Serve non-existent api calls (404 error).
    """
    raise NotFound(detail='Wrong api call.')


def redirect_home(request):
    """
    Redirect to home path URL
    """
    return redirect('/')
