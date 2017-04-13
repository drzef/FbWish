"""
Definition of views.
"""
from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest

from apps.presents.models import Present



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'FbWish/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

'''def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'FbWish/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )'''

'''def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'FbWish/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )'''

def user_home(request):
    """Renders the profile page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'FbWish/user_home.html',
        {
            'title':'User Profile',
            'year':datetime.now().year,
            'uid': request.user.social_auth.get(provider='facebook').uid,
            'own_present': Present.objects.filter(owner=request.user, buyed=False).order_by('-date_inserted'),

        }
    )
