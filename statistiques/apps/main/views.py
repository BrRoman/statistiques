""" apps/statistiques/views.py """

import numpy

from datetime import date
from matplotlib import pyplot
from statistics import mean

from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from .forms import MonkForm
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
        .filter(habit__isnull=False)
        .filter(temporary_profession__isnull=True)
    )
    tempo = len(
        Monk.objects
        .filter(temporary_profession__isnull=False)
        .filter(perpetual_profession__isnull=True)
    )
    perpetual = len(
        Monk.objects
        .filter(perpetual_profession__isnull=False)
    )
    priests = len(
        Monk.objects
        .filter(ordination__isnull=False)
    )

    # Average age
    ages = []
    monks = Monk.objects.all()
    for index, monk in enumerate(monks):
        ages.append((date.today() - monk.birth).days / 365)

    # Histogram:
    hist, bin_edges = numpy.histogram(
        ages,
        bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
    pyplot.figure(figsize=[10, 5])
    result = pyplot.bar([i + 5 for i in bin_edges[:-1]],
                        hist, width=9, color='orange')
    for i, patch in enumerate(list(result)):
        if hist[i] > 0:
            pyplot.text(bin_edges[i] + 5, hist[i] + 1, hist[i],
                        ha='center', va='bottom')
    pyplot.xlim(min(bin_edges), max(bin_edges))
    pyplot.xlabel('Âge', fontsize=10)
    pyplot.ylabel('Nombre de moines', fontsize=10)
    pyplot.xticks(
        numpy.arange(
            min(bin_edges),
            max(bin_edges),
            10),
        fontsize=10
    )
    pyplot.yticks(
        numpy.arange(
            0,
            max(hist) + 5,
            5),
        fontsize=10
    )
    average_age = mean(ages)
    pyplot.text(
        20,
        max(hist) - 5,
        'Moyenne : {:.2f} ans'.format(average_age),
        fontsize=10
    )
    pyplot.savefig(
        '/home/frromain/Sites/statistiques/statistiques/static/img/histogram.svg',
        format='svg',
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


def update(request, **kwargs):
    """ Update a monk. """
    monk = Monk.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        form = MonkForm(request.POST, instance=monk)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('main:home')
            )

    else:
        form = MonkForm(instance=monk)

    print(form)

    return render(
        request,
        'main/form.html',
        {
            'form': form,
            'monk': monk,
        }
    )
