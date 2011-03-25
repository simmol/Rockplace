# Core django imports
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

# Models imports
from users.models import User

def login(request):
  #FIXME add/manage login form
  return render_to_response('users/login.html')


