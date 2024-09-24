from django.db import models

from declassified.models.model_survivor import Survivor
from declassified.models.model_killer import Killer
from declassified.models.model_survivorperk import SurvivorPerk
from declassified.models.model_killerperk import KillerPerk

class DLC(models.Model):
    """ORM for the DLC table in the DLC Database

    Arguments:
        models {class} -- Derived from the base class Model from django.db
    """

    # The DLC Database id
    id = models.AutoField(primary_key=True)

    # The name of the DLC
    name = models.CharField(max_length=50)

    # The list of survivors in the DLC
    survivors = models.ManyToManyField(Survivor)

    # The killer in the DLC
    killers = models.ForeignKey(Killer, on_delete=models.CASCADE)

    # The list of survivor perks in the DLC
    survivor_perks = models.ManyToManyField(SurvivorPerk)

    # The list of killer perks in the DLC
    killer_perks = models.ManyToManyField(KillerPerk)

    # If the chapter is license/paid for
    licensed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def getSurvivors(self):
        list = []
        for survivors in self.survivor_perks.all():
            if survivors.id not in list:
                list.append(survivors.id)
        return list
    
    def getSurvivorPerks(self):
        list = []
        for survivorPerks in self.survivor_perks.all():
            if survivorPerks.id not in list:
                list.append(survivorPerks.id)
        return list
    
    def getKiller(self):
        list = []
        for killers in self.killers.all():
            if killers.id not in list:
                list.append(killers.id)
        return list
    
    def getKillerPerks(self):
        list = []
        for killerPerks in self.killer_perks.all():
            if killerPerks.id not in list:
                list.append(killerPerks.id)
        return list
    
    def getLicensed(self):
        return self.licensed