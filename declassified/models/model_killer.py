from django.db import models

from .model_dlc import DLC
from .model_killerperk import KillerPerk

class Killer(models.Model):
    """ORM for the Survivor table in the Survivor Database

    Arguments:
        models {class} -- Derived from the base class Model from django.db
    """

    # The Survivor Database id
    id = models.AutoField(primary_key=True)

    # The name of the Killer
    name = models.CharField(max_length=30)

    # Nickname of the Killer
    nickname = models.CharField(max_length=15)

    # Killer Power Description
    power = models.TextField()

    # DLC id that the Killer comes from
    dlc_id = models.ForeignKey(DLC,on_delete=models.CASCADE)

    # List of perks that belong to the killer
    killer_perks = models.ManyToManyField(KillerPerk)

    # The rating of this perk from other data sources
    rating = models.DecimalField()

    # The rating of this perk from community members (calculated and displayed out of 5)
    community_rating = models.FloatField()

    # The personal rating of the Survival Guide creator (S to F tier)
    site_rating = models.IntegerField()

    def __str__(self):
        # returns name of killer
        return self.name
    
    def getId(self):
        # returns id of the killer
        return self.id
    
    def getNickname(self):
        # returns the nickname of the killer
        return self.nickname
    
    def getDLCid(self):
        # returns the id of the related dlc
        return self.dlc_id
    
    def getPower(self):
        return self.power
    
    
    def getKillerPerks(self):
        # returns the list of killer perks related to the id
        list = []
        for killerPerks in self.killer_perks.all():
            if killerPerks.id not in list:
                list.append(killerPerks.id)
        return list
    
    def getRating(self):
        # Returns outside rating
        return self.rating
    
    def getCommunity(self):
        # Returns community rating
        return self.community_rating
    
    def getSiteRating(self):
        # Returns site rating
        return self.site_rating