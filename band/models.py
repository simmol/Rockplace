from django.db import models

class Band(models.Model):
  band_name = models.CharField(max_length=100)

  def __unicode__(self):
    return self.band_name
