from django.shortcuts import render_to_response
#from django.http import HttpResponse
from board.models import metrics

def index(request):
    return render_to_response('index.html')

