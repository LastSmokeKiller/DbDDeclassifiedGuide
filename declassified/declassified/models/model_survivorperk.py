from django.db import models


class SurvivorPerk(models.Model):
    """ORM for the Survivor Perks table in the Perk Database

    Arguments:
        models {class} -- Derived from the base class Model from django.db
    """

    # The Standards Database id to a specific Survivor Perk
    id = models.AutoField(primary_key=True)

    # The name of a specific Survivor Perk in the Standard Database
    name = models.CharField(max_length=40)

    # The common name for the Survivor Perk
    common = models.CharField(max_length=15)

    # The Survivor id the perk comes from
    survivor_id = models.ForeignKey('Survivor', on_delete=models.CASCADE)

    # The discription of the Perk
    description = models.TextField()

    # The Use Case of the Perk
    use_case = models.TextField(blank=True)

    # The Best Perk Pairings for this perk and grab that/those ids
    best_pair = models.ManyToManyField("self",blank=True)

    # The explaination on why these perks pair together
    best_exp = models.TextField()

    """ A Neutral pairing ---

        A neutral pairing means that the perk combos could be good
        but could also be bad. This usually depends on how they are used
        and survivor use preference.
    """
    neutral_pair = models.ManyToManyField("self",blank=True)

    # An explaination on why it's a neutral combo
    neutral_exp = models.TextField()

    # Perks that do not pair together
    bad_pair = models.ManyToManyField("self",blank=True)

    # An explaination on why the perks don't pair
    bad_exp = models.TextField()

    # The rating of this perk from other data sources
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    # The rating of this perk from community members (calculated and displayed out of 10)
    community_rating = models.DecimalField(max_digits=3, decimal_places=2)

    # The personal rating of the Survival Guide creator (rating out of 10)
    site_rating = models.IntegerField()


    def __str__(self):
        # Call that returns the name of an object in Surv Perks table
        return self.name

    def getId(self):
        # Call that returns the id of an object in Surv Perks table
        return self.id
    
    def getCommon(self):
        # Call that returns the short name of an object in Surv Perks table
        return self.common
    
    def getSurvivor(self):
        # Call that returns the survivor name who has the perk
        return self.survivor_id
    
    def getDescription(self):
        # returns perk description
        return self.description
    
    def getUseCase(self):
        # returns use case
        return self.use_case
    
    def getBestPair(self):
        # returns best pairing perks
        return self.best_pair
    
    def getBestExp(self):
        # returns best pairing explaination
        return self.best_exp
    
    def getNuetralPair(self):
        # returns neutral pairing perks
        return self.neutral_pair
    
    def getNuetralExp(self):
        # returns neutral pairing explaination
        return self.neutral_exp
    
    def getBadPair(self):
        # returns bad pairing perks
        return self.bad_pair
    
    def getBadExp(self):
        # returns bad pairing explaination
        return self.bad_exp
    
    def getRating(self):
        # Returns outside rating
        return self.rating
    
    def getCommunity(self):
        # Returns community rating
        return self.community_rating
    
    def getSiteRating(self):
        # Returns site rating
        return self.site_rating
    
    