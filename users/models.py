from django.db import models
#
from band.models import Band

class User(models.Model):
  facebook_id = models.IntegerField(primary_key=True)
  band        = models.OneToOneField(Band)

  def __unicode__(self):
    return self.username

  def getFacebookId(self):
    return self.facebook_id
