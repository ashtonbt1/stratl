from datetime import datetime

from django import forms
from django.forms.models import modelformset_factory

from .models import Card, Player, Hitter, Pitcher, Position, RollResult
from .models import MLB_TEAM_CHOICES, CARD_TYPE_CHOICES

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name',)


class HitterForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    season = forms.IntegerField(max_value=datetime.today().year, min_value=1850)
    team = forms.ChoiceField(choices=MLB_TEAM_CHOICES)
    card_type = forms.ChoiceField(choices=CARD_TYPE_CHOICES)
    
    class Meta:
        model = Hitter
        fields = ('parent_player', 'first_name', 'last_name',
                  'season', 'team', 'card_type')


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ('hitter', 'pos', 'fielding', 'error', 'arm', 'pb', 't_err')


class RollResultForm(forms.ModelForm):

    # Constructing custom form, not sure if necessary or if I can
    # get JS to just take the form as is
    # card_id = forms.TextInput(widget=forms.HiddenInput())
    # column = forms.TextInput(widget=forms.HiddenInput())
    # d6_roll = forms.TextInput(widget=forms.HiddenInput())
    # modifier = forms.TextInput()

    class Meta:
        model = RollResult
        fields = ('card', 'column', 'd6_roll', 'modifier',
                  'desc', 'split', 'low', 'high')

BaseRollResultFormSet = modelformset_factory(RollResult, form=RollResultForm, extra=66, can_delete=False)


class RollResultFormSet(BaseRollResultFormSet):
    pass