from django.shortcuts import render
from django.http import HttpResponse


def omlet(request):
    amount = int(request.GET.get('servings', 1))
    rec = {'omlet': {'яйца, шт': 2, 'молоко, л': 0.1, 'соль, ч.л.': 0.5}}
    for key, val in rec['omlet'].items():
        rec['omlet'][key] = val * amount
    return render(request, 'omlet.html', rec)


def pasta(request):
    amount = int(request.GET.get('servings', 1))
    rec = {'pasta': {'макароны, г': 0.3, 'сыр, г': 0.05}}
    for key, val in rec['pasta'].items():
        rec['pasta'][key] = val * amount
    return render(request, 'pasta.html', rec)


def buter(request):
    amount = int(request.GET.get('servings', 1))
    rec = {'buter': {'хлеб, ломтик': 1, 'колбаса, ломтик': 1, 'сыр, ломтик': 1, 'помидор, ломтик': 1}}
    for key, val in rec['buter'].items():
        rec['buter'][key] = val * amount
    return render(request, 'buter.html', rec)


def tort(request):
    amount = int(request.GET.get('servings', 1))
    rec = {'tort': {'dead rat': 3, 'dead cat': 1}}
    for key, val in rec['tort'].items():
        rec['tort'][key] = val * amount
    return render(request, 'tort.html', rec)
