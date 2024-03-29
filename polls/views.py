from django.template import RequestContext, loader
from polls.models import Poll
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html',
        RequestContext(request, {'latest_poll_list': latest_poll_list}))

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', RequestContext(request, {'poll': p}))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
