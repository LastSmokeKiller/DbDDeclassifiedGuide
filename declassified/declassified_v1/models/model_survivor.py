from django.db import models

from .model_dlc import DLC
from .model_survivorperk import SurvivorPerk

class Survivor(models.Model):
    """ORM for the Survivor table in the Survivor Database

    Arguments:
        models {class} -- Derived from the base class Model from django.db
    """

    # The Survivor Database id
    id = models.AutoField(primary_key=True)

    # The name of the Survivor
    name = models.CharField(max_length=30)

    # Nickname of the Survivor
    nickname = models.CharField(max_length=15)

    dlc_id = models.ForeignKey(DLC,on_delete=models.CASCADE)

    survivor_perks = models.ManyToManyField(SurvivorPerk)

    def __str__(self):
        # returns name of the survivor
        return self.name
    
    def getId(self):
        # returns id of the survivor
        return self.id
    
    def getNickname(self):
        # returns the nickname of the survivor
        return self.nickname
    
    def getDLCid(self):
        # returns the id of the related dlc
        return self.dlc_id
    
    def getSurvivorPerks(self):
        # returns the list of survivor perks related to the id
        list = []
        for survivorPerks in self.survivor_perks.all():
            if survivorPerks.id not in list:
                list.append(survivorPerks.id)
        return list
    
    
    
