from django.conf import settings
from django.db import models

# Choice definitions
HAND_CHOICES = (
    ("R", "R"),
    ("L", "L"),
    ("S", "S"),
)

STEAL_RATING_CHOICES = (
    ("A", "A"),
    ("AA", "AA"),
    ("AAA", "AAA"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
)

A_E_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
)

POWER_CHOICES = (
    ("N", "N"),
    ("W", "W"),
)

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

    # Season stats section
    ab = models.PositiveIntegerField(null=False)
    do = models.PositiveIntegerField(null=False)
    tr = models.PositiveIntegerField(null=False)
    hr = models.PositiveIntegerField(null=False)
    bb = models.PositiveIntegerField(null=False)
    so = models.PositiveIntegerField(null=False)
    rbi = models.PositiveIntegerField(null=False)
    bavg = models.DecimalField(max_digits=4, decimal_places=3)
    obp = models.DecimalField(max_digits=4, decimal_places=3)
    slg = models.DecimalField(max_digits=4, decimal_places=3)
    sb = models.PositiveIntegerField(null=False)
    cs = models.PositiveIntegerField(null=False)

    # Hitter card specific info
    bats = models.CharField(null=False, blank=False, choices=HAND_CHOICES,
                            max_length=1)
    power_lhp = models.CharField(null=False, blank=False, choices=POWER_CHOICES,
                            max_length=1)
    power_rhp = models.CharField(null=False, blank=False, choices=POWER_CHOICES,
                            max_length=1)
    steal_auto_lead = models.BooleanField(null=False)
    steal_rating = models.CharField(null=False, blank=False,
                                    choices=STEAL_RATING_CHOICES,
                                    max_length=3)
    steal_good_lead = models.CharField(null=False, blank=True, max_length=50)
    steal_auto_cs = models.CharField(null=False, blank=True, max_length=50)
    steal_primary = models.PositiveIntegerField(null=False)
    steal_primary = models.PositiveIntegerField(null=False)
    bunt = models.CharField(null=False, blank=False, choices=A_E_CHOICES,
                            max_length=1)
    hnr = models.CharField(null=False, blank=False, choices=A_E_CHOICES,
                           max_length=1)
    running = models.PositiveIntegerField(null=False)
    

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

    # Season stats section
    w = models.PositiveIntegerField(null=False)
    l = models.PositiveIntegerField(null=False)
    era = models.DecimalField(max_digits=5, decimal_places=2)
    ip = models.PositiveIntegerField(null=False)
    hits = models.PositiveIntegerField(null=False)
    walks = models.PositiveIntegerField(null=False)
    ks = models.PositiveIntegerField(null=False)
    hr = models.PositiveIntegerField(null=False)
    gs = models.PositiveIntegerField(null=False)
    sv = models.PositiveIntegerField(null=False)

    # Pitcher card specific info
    throws = models.CharField(null=False, blank=False, choices=HAND_CHOICES,
                              max_length=1)
    starter = models.PositiveIntegerField(null=True)
    relief = models.PositiveIntegerField(null=True)
    closer = models.CharField(max_length=1, null=False, blank=True)
    starred = models.BooleanField(null=True)
    starter_first = models.BooleanField(null=False)
    bats = models.CharField(null=False, blank=False, max_length=4)
    hold = models.IntegerField(null=False)
    fielding = models.PositiveIntegerField(null=False)
    error = models.PositiveIntegerField(null=False)
    bk = models.PositiveIntegerField(null=False)
    wp = models.PositiveIntegerField(null=False)
    bunt = models.CharField(null=False, blank=False, choices=A_E_CHOICES,
                            max_length=1)    
        
    # Numbers that need to be hunted down
    injury = models.PositiveIntegerField(null=True)
    steal_auto_lead = models.BooleanField(null=False)
    steal_rating = models.CharField(null=False, blank=False,
                                    choices=STEAL_RATING_CHOICES,
                                    max_length=3)
    steal_good_lead = models.CharField(null=True, blank=True, max_length=50)
    steal_auto_cs = models.CharField(null=True, blank=True, max_length=50)
    steal_primary = models.PositiveIntegerField(null=True)
    steal_primary = models.PositiveIntegerField(null=True)
    running = models.PositiveIntegerField(null=True)

    def __str__(self):
        suffix = f" - {self.card_type}" if self.card_type != 'Standard' else ""
        return f"{self.first_name} {self.last_name} ({self.team} {self.season}{suffix})"
    
    def __repr__(self):
        return f"<{type(self)}> {self.last_name}, {self.first_name} ({self.team} {self.season} - {self.card_type})"
    
    class Meta:
        ordering = ['last_name', 'first_name', 'season', 'team', 'card_type']