""" apps/statistiques/views.py """

from django.shortcuts import render

from .models import Moine


def home(request):
    """ Home view of statistiques. """
    monks = Moine.objects.all().order_by('entry')
    return render(
        request,
        'main/home.html',
        {
            'monks': monks,
        }
    )
