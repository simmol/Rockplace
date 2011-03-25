from django.conf.urls.defaults import *
from users.models import User

info_dict = {
  'queryset': User.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'users.views.login'),
)
