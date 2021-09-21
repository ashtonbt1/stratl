from django.shortcuts import redirect, render, get_object_or_404
from tablib import Dataset

from .models import Player
from .forms import PlayerForm
from .resources import PlayerResource

# Create your views here.
def player_list(request):
    players = Player.objects.all()
    return render(request, 'league/player_list.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'league/player_detail.html', {'player': player})

def player_new(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm()
    return render(request, 'league/player_edit.html', {'form': form})

def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'league/player_edit.html', {'form': form})

def simple_upload(request):
    if request.method == 'POST':
        player_resource = PlayerResource()
        dataset = Dataset()
        new_players = request.FILES['importfile']

        imported_data = dataset.load(new_players.read())
        result = player_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            player_resource.import_data(dataset, dry_run=False)
    
    return render(request, 'league/simple_upload.html')