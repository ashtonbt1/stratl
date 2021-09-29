from django import forms
from django.forms.models import modelformset_factory

from .models import Card, Player, Hitter, Pitcher, Position, RollResult

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name',)


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
    
    def __init__(self, *args, **kwargs):
        self.card_id = kwargs.pop('card_id')
        super(RollResultForm, self).__init__(*args, **kwargs)

        self.fields['card'].queryset = Card.objects.filter(id=self.card_id)

BaseRollResultFormSet = modelformset_factory(RollResult, form=RollResultForm, extra=66, can_delete=False)


class RollResultFormSet(BaseRollResultFormSet):

    def __init__(self, *args, **kwargs):
        self.card_id = kwargs.pop('card_id')
        super(RollResultFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False
        
    def _construct_form(self, *args, **kwargs):
        # Inject user in each form on the formset
        kwargs['card_id'] = self.card_id
        return super(RollResultFormSet, self)._construct_form(*args, **kwargs)