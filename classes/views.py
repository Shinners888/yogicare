from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Classes


def all_classes(request):

    classes = Classes.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes.html', context)


def classe_detail(request, classe_id):

    classe = get_object_or_404(Classes, pk=classe_id)

    context = {
        'classe': classe,
    }

    return render(request, 'classes/classe_detail.html', context)