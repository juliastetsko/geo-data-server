from django.contrib.gis.db import models as gis_models
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    location = gis_models.PointField(srid=4326)

    def __str__(self):
        return self.name


