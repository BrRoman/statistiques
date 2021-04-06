""" apps/statistiques/views.py """

from django.shortcuts import render

from .models import Monk


def home(request):
    """ Home view of statistiques. """
    list_of_monks = Monk.objects.all().order_by('entry')
    postulants = len(
        Monk.objects
        .filter(habit__isnull=True)
    )
    novices = len(
        Monk.objects
        .filter(temporary_profession__isnull=True)
        .filter(habit__isnull=False)
    )
    tempo = len(
        Monk.objects
        .filter(perpetual_profession__isnull=True)
        .filter(temporary_profession__isnull=False)
    )
    perpetual = len(
        Monk.objects
        .filter(perpetual_profession__isnull=False)
    )
    priests = len(
        Monk.objects
        .filter(ordination__isnull=False)
    )
    return render(
        request,
        'main/home.html',
        {
            'list_of_monks': list_of_monks,
            'monks': len(list_of_monks),
            'postulants': postulants,
            'novices': novices,
            'tempo': tempo,
            'perpetual': perpetual,
            'priests': priests,
        }
    )
