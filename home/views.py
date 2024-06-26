from django.shortcuts import render
from django.http import Http404


def home(request):
    """
    View to render the landing page
    """
    template = 'home/index.html'

    # return render(request, template)
    raise Http404("Page not found")
