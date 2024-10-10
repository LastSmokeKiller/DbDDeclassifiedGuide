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

    # If the chapter is license/paid for
    licensed = models.BooleanField(default=False)

    # Is this dlc free with the game
    free = models.BooleanField(default=False)

    # Can this dlc still be purchased
    dlc_buy = models.BooleanField(default=True)

    # the cost of real money for dlc
    dollar_cost = models.FloatField()

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
    
    def getKiller(self):
        list = []
        for killers in self.killers.all():
            if killers.id not in list:
                list.append(killers.id)
        return list
    
    def getLicensed(self):
        return self.licensed
    
    def getFree(self):
        return self.free