""" apps/statistiques/views.py """

from django.shortcuts import render


def home(request):
    """ Home view of statistiques. """
    return render(request, 'main/home.html')
