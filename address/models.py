from django.db import models


class Address(models.Model):
    zip_code = models.CharField(max_length=5, blank=True)
    country = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    house = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return "%s, %s, %s" % (self.zip_code, self.country, self.province)