from django.core.paginator import Paginator
from django.forms.formsets import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from tablib import Dataset

from .models import Player, Position, Hitter, Card, RollResult
from .forms import HitterForm, PlayerForm, PositionForm, RollResultForm, RollResultFormSet
from .resources import PlayerResource

# Create your views here.
def player_list(request):
    players = Player.objects.all()
    paginator = Paginator(players, 20)

    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'league/player_list.html', {'page_obj': page_obj})

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

def hitter_new(request):
    if request.method == 'POST':
        form = HitterForm(request.POST)
        if form.is_valid():
            hitter = form.save(commit=False)
            hitter.save()
            return redirect('hitter_detail', pk=hitter.pk)
    else:
        form = HitterForm()
    return render(request, 'league/hitter_edit.html', {'form': form})

def hitter_detail(request, pk):
    hitter = get_object_or_404(Hitter, pk=pk)
    positions = Position.objects.filter(hitter=hitter.pk)
    roll_results = RollResult.objects.filter(card=hitter.pk)
    return render(request, 'league/hitter_detail.html',
                    {
                        'hitter': hitter,
                        'positions': positions,
                        'roll_results': roll_results,
                    })

def generate_init_vals_roll_results(pk):
    ilist = list()
    nforms = 66
    nrows = 11
    for i in range(nforms):
        col = int(i / nrows) + 1
        row = (i % nrows) + 2
        form_dict = {
            'card': pk,
            'column': col,
            'd6_roll': row
        }
        ilist.append(form_dict)
    return ilist

def build_card_results(request, pk):
    RollResultFormSet = formset_factory(RollResultForm, extra=66, max_num=66)
    if request.method == 'POST':
        formset = RollResultFormSet(request.POST)
        if formset.is_valid():
            hitter = get_object_or_404(Hitter, pk=pk)
            return redirect('hitter_detail', pk=hitter.pk)
    else:
        init_list = generate_init_vals_roll_results(pk)
        formset = RollResultFormSet(initial=init_list)
    return render(request, 'league/rollresult_edit.html', {'formset': formset})