# Generated by Django 2.2.24 on 2021-09-21 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Pitcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('season', models.PositiveIntegerField()),
                ('team', models.CharField(max_length=5)),
                ('card_type', models.CharField(max_length=50)),
                ('w', models.PositiveIntegerField()),
                ('l', models.PositiveIntegerField()),
                ('era', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ip', models.PositiveIntegerField()),
                ('hits', models.PositiveIntegerField()),
                ('walks', models.PositiveIntegerField()),
                ('ks', models.PositiveIntegerField()),
                ('hr', models.PositiveIntegerField()),
                ('gs', models.PositiveIntegerField()),
                ('sv', models.PositiveIntegerField()),
                ('throws', models.CharField(choices=[('R', 'R'), ('L', 'L'), ('S', 'S')], max_length=1)),
                ('starter', models.PositiveIntegerField(null=True)),
                ('relief', models.PositiveIntegerField(null=True)),
                ('closer', models.CharField(blank=True, max_length=1)),
                ('starred', models.BooleanField(null=True)),
                ('starter_first', models.BooleanField()),
                ('bats', models.CharField(max_length=4)),
                ('hold', models.IntegerField()),
                ('fielding', models.PositiveIntegerField()),
                ('error', models.PositiveIntegerField()),
                ('bk', models.PositiveIntegerField()),
                ('wp', models.PositiveIntegerField()),
                ('bunt', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('injury', models.PositiveIntegerField(null=True)),
                ('steal_auto_lead', models.BooleanField()),
                ('steal_rating', models.CharField(choices=[('A', 'A'), ('AA', 'AA'), ('AAA', 'AAA'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=3)),
                ('steal_good_lead', models.CharField(blank=True, max_length=50, null=True)),
                ('steal_auto_cs', models.CharField(blank=True, max_length=50, null=True)),
                ('steal_primary', models.PositiveIntegerField(null=True)),
                ('running', models.PositiveIntegerField(null=True)),
                ('parent_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Player')),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'season', 'team', 'card_type'],
            },
        ),
        migrations.CreateModel(
            name='Hitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('season', models.PositiveIntegerField()),
                ('team', models.CharField(max_length=5)),
                ('card_type', models.CharField(max_length=50)),
                ('ab', models.PositiveIntegerField()),
                ('do', models.PositiveIntegerField()),
                ('tr', models.PositiveIntegerField()),
                ('hr', models.PositiveIntegerField()),
                ('bb', models.PositiveIntegerField()),
                ('so', models.PositiveIntegerField()),
                ('rbi', models.PositiveIntegerField()),
                ('bavg', models.DecimalField(decimal_places=3, max_digits=4)),
                ('obp', models.DecimalField(decimal_places=3, max_digits=4)),
                ('slg', models.DecimalField(decimal_places=3, max_digits=4)),
                ('sb', models.PositiveIntegerField()),
                ('cs', models.PositiveIntegerField()),
                ('bats', models.CharField(choices=[('R', 'R'), ('L', 'L'), ('S', 'S')], max_length=1)),
                ('power_lhp', models.CharField(choices=[('N', 'N'), ('W', 'W')], max_length=1)),
                ('power_rhp', models.CharField(choices=[('N', 'N'), ('W', 'W')], max_length=1)),
                ('steal_auto_lead', models.BooleanField()),
                ('steal_rating', models.CharField(choices=[('A', 'A'), ('AA', 'AA'), ('AAA', 'AAA'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=3)),
                ('steal_good_lead', models.CharField(blank=True, max_length=50)),
                ('steal_auto_cs', models.CharField(blank=True, max_length=50)),
                ('steal_primary', models.PositiveIntegerField()),
                ('bunt', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('hnr', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('running', models.PositiveIntegerField()),
                ('parent_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Player')),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'season', 'team', 'card_type'],
            },
        ),
    ]
