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

MLB_TEAM_CHOICES = (
    ('ANA', 'Anaheim'),
    ('ARI', 'Arizona'),
    ('ATL', 'Atlanta'),
    ('BAL', 'Baltimore'),
    ('BOB', 'Boston Beaneaters/Braves'),
    ('BOD', 'Boston Doves'),
    ('BOS', 'Boston'),
    ('BKN', 'Brooklyn'),
    ('CAL', 'California'),
    ('CHC', 'Chicago Cubs'),
    ('CHO', 'Chicago Orphans'),
    ('CWS', 'Chicago White Sox'),
    ('CIN', 'Cincinnati'),
    ('CLE', 'Cleveland'),
    ('COL', 'Colorado'),
    ('DET', 'Detroit'),
    ('FLA', 'Florida'),
    ('HOU', 'Houston'),
    ('KCA', 'Kansas City Athletics'),
    ('KCR', 'Kansas City Royals'),
    ('LAA', 'Los Angeles Angels'),
    ('LAD', 'Los Angeles Dodgers'),
    ('MIA', 'Miami'),
    ('MIL', 'Milwaukee'),
    ('MTL', 'Montreal'),
    ('NYG', 'New York Giants/Gothams'),
    ('NYH', 'New York Highlanders'),
    ('NYM', 'New York Mets'),
    ('NYY', 'New York Yankees'),
    ('OAK', 'Oakland'),
    ('PHA', 'Philadelphia Athletics'),
    ('PHI', 'Philadelphia Phillies'),
    ('PIT', 'Pittsburgh'),
    ('SDP', 'San Diego'),
    ('SEA', 'Seattle'),
    ('SFG', 'San Francisco'),
    ('SLB', 'St Louis Browns'),
    ('STL', 'St Louis Cardinals'),
    ('TBR', 'Tampa Bay'),
    ('TEX', 'Texas'),
    ('TOR', 'Toronto'),
    ('WSH', 'Washington'),
)

CARD_TYPE_CHOICES = (
    ('Standard', 'Standard'),
    ('Secondary', 'Secondary'),
    ('Pitcher Hitting', 'Pitcher Hitting'),
    ('Custom', 'Custom'),
)

POWER_CHOICES = (
    ("N", "N"),
    ("W", "W"),
)

POS_CHOICES = (
    ("C", "C"),
    ("1B", "1B"),
    ("2B", "2B"),
    ("3B", "3B"),
    ("SS", "SS"),
    ("LF", "LF"),
    ("CF", "CF"),
    ("RF", "RF"),
)

ROLLMOD_CHOICES = (
    ("N", "Normal"),
    ("S", "Split"),
    ("BS", "Ballpark Single"),
    ("BO", "Ballpark Open"),
    ("BH", "Ballpark HR"),
    ("BHS", "Ballpark HR Split"),
    ("INJ", "Injury Chance"),
    ("C", "Clutch"),
    ("F", "Fatigue"),
)

ROLLRESULT_CHOICES = (
    ("CATCH-X", "CATCH-X"),
	("DO", "DO"),
	("DOUBLE**", "DOUBLE**"),
	("DO**", "DO**"),
	("DOUBLE (cf)", "DOUBLE (cf)"),
	("DOUBLE (lf)", "DOUBLE (lf)"),
	("DOUBLE (rf)", "DOUBLE (rf)"),
	("FLY (cf) X", "FLY (cf) X"),
	("FLY (lf) X", "FLY (lf) X"),
	("FLY (rf) X", "FLY (rf) X"),
	("GB (1b) X", "GB (1b) X"),
	("GB (2b) X", "GB (2b) X"),
	("GB (3b) X", "GB (3b) X"),
	("GB (p) X", "GB (p) X"),
	("GB (ss) X", "GB (ss) X"),
	("HBP", "HBP"),
	("HOMERUN", "HOMERUN"),
	("HR", "HR"),
	("N-HR", "N-HR"),
	("SI*", "SI*"),
	("SI**", "SI**"),
	("SINGLE (cf)", "SINGLE (cf)"),
	("SINGLE (lf)", "SINGLE (lf)"),
	("SINGLE (rf)", "SINGLE (rf)"),
	("SINGLE*", "SINGLE*"),
	("SINGLE**", "SINGLE**"),
	("TR", "TR"),
	("TRIPLE", "TRIPLE"),
	("WALK", "WALK"),
	("fly (cf) A", "fly (cf) A"),
	("fly (cf) B", "fly (cf) B"),
	("fly (cf) B?", "fly (cf) B?"),
	("fly (cf) C", "fly (cf) C"),
	("fly (lf) B", "fly (lf) B"),
	("fly (lf) B?", "fly (lf) B?"),
	("fly (lf) C", "fly (lf) C"),
	("fly (rf) A", "fly (rf) A"),
	("fly (rf) B", "fly (rf) B"),
	("fly (rf) B?", "fly (rf) B?"),
	("fly (rf) C", "fly (rf) C"),
	("foulout (1b)", "foulout (1b)"),
	("foulout (3b)", "foulout (3b)"),
	("foulout (c)", "foulout (c)"),
	("gb (1b) A", "gb (1b) A"),
	("gb (1b) A+", "gb (1b) A+"),
	("gb (1b) B", "gb (1b) B"),
	("gb (1b) C", "gb (1b) C"),
	("gb (2b) A", "gb (2b) A"),
	("gb (2b) A+", "gb (2b) A+"),
	("gb (2b) B", "gb (2b) B"),
	("gb (2b) B+", "gb (2b) B+"),
	("gb (2b) C", "gb (2b) C"),
	("gb (3b) A", "gb (3b) A"),
	("gb (3b) B", "gb (3b) B"),
	("gb (p) A", "gb (p) A"),
	("gb (p) B", "gb (p) B"),
	("gb (ss) A", "gb (ss) A"),
	("gb (ss) A+", "gb (ss) A+"),
	("gb (ss) B", "gb (ss) B"),
	("gb (ss) B+", "gb (ss) B+"),
	("lineout (1b)", "lineout (1b)"),
	("lineout (2b)", "lineout (2b)"),
	("lineout (3b)", "lineout (3b)"),
	("lineout (ss)", "lineout (ss)"),
	("lo", "lo"),
	("lo (1b)", "lo (1b)"),
	("lo (1b) max", "lo (1b) max"),
	("lo (2b)", "lo (2b)"),
	("lo (2b) max", "lo (2b) max"),
	("lo (3b)", "lo (3b)"),
	("lo (3b) max", "lo (3b) max"),
	("lo (ss)", "lo (ss)"),
	("lo (ss) max", "lo (ss) max"),
	("popout (1b)", "popout (1b)"),
	("popout (2b)", "popout (2b)"),
	("popout (3b)", "popout (3b)"),
	("popout (ss)", "popout (ss)"),
	("strikeout", "strikeout"),
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


class Card(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    season = models.PositiveIntegerField(null=False)
    team = models.CharField(null=False, blank=False, max_length=5)
    card_type = models.CharField(null=False, blank=False, max_length=50)
    parent_player = models.ForeignKey(Player, on_delete=models.CASCADE)

class Hitter(Card):
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
    steal_secondary = models.PositiveIntegerField(null=False)
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


class Pitcher(Card):
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
    steal_secondary = models.PositiveIntegerField(null=True)
    running = models.PositiveIntegerField(null=True)

    def __str__(self):
        suffix = f" - {self.card_type}" if self.card_type != 'Standard' else ""
        return f"{self.first_name} {self.last_name} ({self.team} {self.season}{suffix})"
    
    def __repr__(self):
        return f"<{type(self)}> {self.last_name}, {self.first_name} ({self.team} {self.season} - {self.card_type})"
    
    class Meta:
        ordering = ['last_name', 'first_name', 'season', 'team', 'card_type']


class Position(models.Model):
    hitter = models.ForeignKey(Hitter, on_delete=models.CASCADE)
    pos = models.CharField(null=False, blank=False, choices=POS_CHOICES, max_length=2)
    fielding = models.PositiveIntegerField(null=False)
    error = models.PositiveIntegerField(null=False)
    arm = models.IntegerField(null=True, blank=True)
    pb = models.IntegerField(null=True, blank=True)
    t_err = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.arm:
            pos_str = f"{self.pos.lower()}-{self.fielding} ({self.arm}) e{self.error}"
        else:
            pos_str = f"{self.pos.lower()}-{self.fielding} e{self.error}"
        if self.pb and self.t_err:
            pos_str = pos_str + f", T-1-{self.t_err} (pb-{self.pb})"
        return pos_str
    
    def __repr__(self):
        return f"<{type(self)}> {self}"


class RollResult(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    column = models.PositiveIntegerField(null=False)
    d6_roll = models.PositiveIntegerField(null=False)
    modifier = models.CharField(blank=True, null=True, choices=ROLLMOD_CHOICES, max_length=5)
    desc = models.CharField(blank=True, null=True, choices=ROLLRESULT_CHOICES, max_length=60)
    split = models.PositiveIntegerField(blank=True, null=True)
    low = models.CharField(blank=True, null=True, choices=ROLLRESULT_CHOICES, max_length=60)
    high = models.CharField(blank=True, null=True, choices=ROLLRESULT_CHOICES, max_length=60)

    def __str__(self):
        summary = f"{self.column}-{self.column:02}:"
        if self.modifier:
            summary = summary + f" ({self.modifier})"
        if self.desc:
            summary = summary + f" {self.desc}"
        if self.low:
            summary = summary + f"; {self.low}"
        if self.split:
            summary = summary + f"|{self.split}|{self.high}"
        return summary
    
    def __repr__(self):
        return f"<{type(self)}> {self}"