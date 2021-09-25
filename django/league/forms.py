from django import forms

from .models import Player, Hitter, Pitcher, Position

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name',)


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ('hitter', 'pos', 'fielding', 'error', 'arm', 'pb', 't_err')
