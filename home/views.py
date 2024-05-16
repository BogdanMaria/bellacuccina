from django.shortcuts import render

def home(request):
    """
    View to render the landing page
    """
    template = 'home/index.html'

    return render(request, template)
