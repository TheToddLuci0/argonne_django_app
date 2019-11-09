from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def mail(request):
    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'mail.html', context)

@login_required()
def hmi(request):
    context = {
        'hmi': '10.0.%s.9' % settings.TEAM,
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'hmi.html', context)

@login_required()
def notes(request):
    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM,
        'myip': '10.0.%s.6' % settings.TEAM
    }
    return render(request, 'notes.html', context)

@login_required()
def files(request):
    context = {
        'ftpsrv': '10.0.%s.8' % settings.TEAM
    }
    return render(request, 'files.html', context)


def index(request):
    if request.user.is_authenticated:
        context = {
            'ftpsrv': '10.0.%s.8' % settings.TEAM
        }
    else:
        context = {}
    return render(request, 'home.html', context)
