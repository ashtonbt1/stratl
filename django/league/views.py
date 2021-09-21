from django.shortcuts import render
from .models import Player

# Create your views here.
def player_list(request):
    players = Player.objects.all()
    return render(request, 'league/player_list.html', {'players': players})