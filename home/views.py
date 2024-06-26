from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import PermissionDenied


def home(request):
    """
    View to render the landing page
    """
    template = 'home/index.html'

    return render(request, template)
    
