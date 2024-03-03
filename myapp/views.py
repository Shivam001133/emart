from django.shortcuts import render


def home(request):
    return render(request, 'emat.nav.html')
