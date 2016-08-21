from django.http import HttpResponseNotFound
from django.shortcuts import redirect


def wrong_api_call(request):
    """
    Serve non-existent api calls (404 error).
    """
    return HttpResponseNotFound('Wrong api call.')


def redirect_home(request):
    """
    Redirect to home path URL
    """
    return redirect('/')
