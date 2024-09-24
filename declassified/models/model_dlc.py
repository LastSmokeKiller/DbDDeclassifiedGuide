from django.db import models

from declassified.models.model_survivor import Survivor

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
    survivor = models.ManyToManyField(Survivor)