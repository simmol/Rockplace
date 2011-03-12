# Django imports
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

# Models imports
from polls.models import Poll

def index(request):
  latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]

  return render_to_response('polls/index.html', {'latest_poll_list':latest_poll_list}) 

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id) 
    return  render_to_response('polls/details.html', {'poll':poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
