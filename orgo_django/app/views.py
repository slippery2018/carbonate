from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

## url(r'^$', views.index, name='index'),
def index(request):
    context = {}
    return render(request, 'app/index.html', context)