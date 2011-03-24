from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=200)
  facebook_id =  models.CharField(max_length=50)

  def __unicode__(self):
    return self.username

  def getFacebookId(self):
    return self.facebook_id

