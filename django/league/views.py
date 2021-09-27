from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from tablib import Dataset

from .models import Player, Position, Hitter
from .forms import PlayerForm, PositionForm, RollResultFormSet
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

def position_new(request, pk):
    hitter = get_object_or_404(Hitter, pk=pk)
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.save()
            return redirect('player_detail', pk=hitter.parent_player.pk)
    else:
        form = PositionForm(initial={'hitter': hitter.pk})
    return render(request, 'league/position_edit.html', {'form': form, 'hitter': hitter})

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

def build_card_results(request, card_id):
    if request.method == 'POST':
        formset = RollResultFormSet(card_id=card_id, data=request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = RollResultFormSet(card_id=card_id)
    return render_to_response('rollresult_edit.html', {'formset': formset})