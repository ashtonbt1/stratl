# Generated by Django 2.2.24 on 2021-09-20 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('season', models.PositiveIntegerField()),
                ('team', models.CharField(max_length=5)),
                ('card_type', models.CharField(max_length=50)),
                ('parent_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Player')),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'season', 'team', 'card_type'],
            },
        ),
    ]