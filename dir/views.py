from django.shortcuts import render
from django.http import Http404
from .models import Tournament,Motion


def index(request):
    all_tournaments = Tournament.objects.all().order_by('-date')
    yrs = []
    for i in all_tournaments.values_list('date__year', flat=True).distinct():
        if not i in yrs:
            yrs.append(i)

    ln = request.GET.get('Lang')
    fmt = request.GET.get('Format')
    if ln and ln != 'both':
        all_tournaments = all_tournaments.filter(lang=ln).order_by('-date')
    if fmt and fmt != 'all':
        all_tournaments = all_tournaments.filter(format=fmt).order_by('-date')

    context = {'all_tournaments': all_tournaments, 'all_years': yrs, 'ln': ln, 'fmt': fmt}
    return render(request, 'dir/index.html', context)


def motion_by_year(request, yr):
    all_tournaments = Tournament.objects.filter(date__year=yr).order_by('-date')
    ln = request.GET.get('Lang')
    fmt = request.GET.get('Format')
    if ln and ln != 'both':
        all_tournaments = all_tournaments.filter(lang=ln).order_by('-date')
    if fmt and fmt != 'all':
        all_tournaments = all_tournaments.filter(format=fmt).order_by('-date')
    context = {'all_tournaments': all_tournaments, 'ln': ln, 'fmt': fmt, 'yr':yr}
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
    all_tournaments = Tournament.objects.all()
    ln = request.GET.get('Lang')
    fmt = request.GET.get('Format')
    keyword = request.GET.get('keyword')
    if ln and ln != 'both':
        all_tournaments = all_tournaments.filter(lang=ln).order_by('-date')
    if fmt and fmt != 'all':
        all_tournaments = all_tournaments.filter(format=fmt).order_by('-date')
    context = {'all_tournaments': all_tournaments, 'ln': ln, 'fmt': fmt}
    return render(request, 'dir/search.html', context)


