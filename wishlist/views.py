from django.shortcuts import render


def wishlist(request):
    """
    view to render the wishlist page
    """
    template = 'wishlist/wishlist.html'
    # context = {}
    return render(request, template)