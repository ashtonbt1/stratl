from django.conf import settings
from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.CharField(primary_key=True, null=False, blank=False, unique=True, max_length=25)
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)

    @property
    def bbref_link(self):
        """Returns player's BBRef link"""
        return f"https://www.baseball-reference.com/players/{self.id[0]}/{self.id}.shtml"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"<{type(self)}> {self.last_name}, {self.first_name} ({self.id})"
    
    class Meta:
        ordering = ['last_name', 'first_name', 'id']


class Hitter(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    season = models.PositiveIntegerField(null=False)
    team = models.CharField(null=False, blank=False, max_length=5)
    card_type = models.CharField(null=False, blank=False, max_length=50)
    parent_player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        suffix = f" - {self.card_type}" if self.card_type != 'Standard' else ""
        return f"{self.first_name} {self.last_name} ({self.team} {self.season}{suffix})"
    
    def __repr__(self):
        return f"<{type(self)}> {self.last_name}, {self.first_name} ({self.team} {self.season} - {self.card_type})"
    
    class Meta:
        ordering = ['last_name', 'first_name', 'season', 'team', 'card_type']


class Pitcher(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    season = models.PositiveIntegerField(null=False)
    team = models.CharField(null=False, blank=False, max_length=5)
    card_type = models.CharField(null=False, blank=False, max_length=50)
    parent_player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        suffix = f" - {self.card_type}" if self.card_type != 'Standard' else ""
        return f"{self.first_name} {self.last_name} ({self.team} {self.season}{suffix})"
    
    def __repr__(self):
        return f"<{type(self)}> {self.last_name}, {self.first_name} ({self.team} {self.season} - {self.card_type})"
    
    class Meta:
        ordering = ['last_name', 'first_name', 'season', 'team', 'card_type']