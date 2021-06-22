from django.shortcuts import render
from AutotestWebD.settings import *

def index(request):
    context = {"SITE_NAME": SITE_NAME}
    return render(request, 'index.html', context)
