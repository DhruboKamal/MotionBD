from django.shortcuts import render
from django.http import Http404
from .models import Tournament,Motion


def index(request):
    all_motions = Motion.objects.all().order_by('-tournament__date')
    yrs = []
    for i in all_motions.values_list('tournament__date__year', flat=True).distinct():
        if not i in yrs:
            yrs.append(i)

    ln = request.GET.get('Lang')
    fmt = request.GET.get('Format')
    if ln and ln != 'both':
        all_motions = all_motions.filter(tournament__lang=ln).order_by('-tournament__date')
    if fmt and fmt != 'all':
        all_motions = all_motions.filter(tournament__lang=ln).order_by('-tournament__date')

    context = {'all_motions': all_motions, 'ln': ln, 'fmt': fmt, 'all_years': yrs}
    return render(request, 'dir/index.html', context)


def motion_by_year(request, yr):
    all_motions = Motion.objects.all().order_by('-tournament__date')
    ln = request.GET.get('Lang')
    fmt = request.GET.get('Format')
    if ln and ln != 'both':
        all_motions = all_motions.filter(tournament__lang=ln).order_by('-tournament__date')
    if fmt and fmt != 'all':
        all_motions = all_motions.filter(tournament__lang=ln).order_by('-tournament__date')

    context = {'all_motions': all_motions, 'ln': ln, 'fmt': fmt}
    return render(request, 'dir/motionsbyyear.html', context)


def tournaments(request):
    all_tournaments = Tournament.objects.all()
    ln = request.GET.get('Lang')
    fmt = request.GET.get('Format')
    if ln and ln != 'both':
        all_tournaments = all_tournaments.filter(lang=ln).order_by('-date')
    if fmt and fmt != 'all':
        all_tournaments = all_tournaments.filter(format=fmt).order_by('-date')
    context = {'all_tournaments': all_tournaments, 'ln': ln, 'fmt': fmt}
    return render(request, 'dir/tournaments.html', context)


def tournament_details(request, tournament_id):
    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except 'Tournament not found':
        raise Http404("Tournament not found")
    return render(request, 'dir/tournament_details.html', {'tournament': tournament})


def search(request):
    all_motions = Motion.objects.all().order_by('-tournament__date')
    ln = request.GET.get('Lang')
    fmt = request.GET.get('Format')
    kw = request.GET.get('KeyWord')
    if ln and ln != 'both':
        all_motions = all_motions.filter(tournament__lang=ln)
    if fmt and fmt != 'all':
        all_motions = all_motions.filter(tournament__lang=ln)
    if kw:
        all_motions = all_motions.filter(motion_text__contains=kw)
    context = {'all_motions': all_motions, 'ln': ln, 'fmt': fmt}
    return render(request, 'dir/search.html', context)


