from django.contrib.gis.db import models


class Address(models.Model):
    plz = models.CharField(max_length=6, blank=False, null=False)
    street = models.CharField(max_length=120, blank=True, null=True)
    house = models.IntegerField(blank=True, null=True)
    geo_point = models.PointField(srid=4326, blank=False, null=False)

    def __str__(self):
        return str(self.geo_point)

    class Meta:
        verbose_name = 'Adresse'
        verbose_name_plural = 'Adresse'
