from django import forms

from .models import Player, Hitter, Pitcher

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name',)