from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import  Tournament


def index(request):
    all_tournaments = Tournament.objects.all().order_by('-date')

    return render(request, 'dir/index.html', {'all_tournaments': all_tournaments, })


def tournaments(request):
    all_tournaments = Tournament.objects.all()
    return render(request, 'dir/tournaments.html', {'all_tournaments': all_tournaments, })


def tournament_details(request, tournament_id):
    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except:
        raise Http404("Tournament not found")
    return render(request, 'dir/tournament_details.html', {'tournament': tournament})
