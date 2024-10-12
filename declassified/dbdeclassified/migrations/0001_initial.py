# Generated by Django 5.1.1 on 2024-10-11 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IridescentCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_level', models.IntegerField()),
                ('current_iridescent', models.IntegerField()),
                ('currrent_xp', models.IntegerField()),
                ('iridescent_needed', models.IntegerField()),
                ('xpon', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Survivor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='KillerPerk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('common', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('use_case', models.TextField(blank=True)),
                ('best_exp', models.TextField()),
                ('neutral_exp', models.TextField()),
                ('bad_exp', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('community_rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('site_rating', models.IntegerField()),
                ('bad_pair', models.ManyToManyField(blank=True, to='dbdeclassified.killerperk')),
                ('best_pair', models.ManyToManyField(blank=True, to='dbdeclassified.killerperk')),
                ('neutral_pair', models.ManyToManyField(blank=True, to='dbdeclassified.killerperk')),
            ],
        ),
        migrations.CreateModel(
            name='Killer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=15)),
                ('power', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('community_rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('site_rating', models.IntegerField()),
                ('killer_perks', models.ManyToManyField(to='dbdeclassified.killerperk')),
            ],
        ),
        migrations.CreateModel(
            name='DLC',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('licensed', models.BooleanField(default=False)),
                ('free', models.BooleanField(default=False)),
                ('dlc_buy', models.BooleanField(default=True)),
                ('dollar_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('killers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbdeclassified.killer')),
                ('survivors', models.ManyToManyField(to='dbdeclassified.survivor')),
            ],
        ),
        migrations.CreateModel(
            name='SurvivorPerk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('common', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('use_case', models.TextField(blank=True)),
                ('best_exp', models.TextField()),
                ('neutral_exp', models.TextField()),
                ('bad_exp', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('community_rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('site_rating', models.IntegerField()),
                ('bad_pair', models.ManyToManyField(blank=True, to='dbdeclassified.survivorperk')),
                ('best_pair', models.ManyToManyField(blank=True, to='dbdeclassified.survivorperk')),
                ('neutral_pair', models.ManyToManyField(blank=True, to='dbdeclassified.survivorperk')),
            ],
        ),
        migrations.AddField(
            model_name='survivor',
            name='survivor_perks',
            field=models.ManyToManyField(to='dbdeclassified.survivorperk'),
        ),
    ]
