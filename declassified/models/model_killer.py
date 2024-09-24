from django.db import models

from .model_dlc import DLC
from .model_killerperk import 

class Killer(models.Model):
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

    licensed = models.BooleanField()

    def __str__(self):
        # returns name of character
        return self.name
    
    def getId(self):

        return self.id
    
    def getNickname(self):

        return self.nickname
    
    def getDLCid(self):

        return self.dlc_id
    
    def getSurvivorPerks(self):

        return self.survivor_perks
    
    def getLicense(self):

        return self.licensed