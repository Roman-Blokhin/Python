from django.shortcuts import render


def index(request):
    data = {

    }
    return render(request, 'projects/index,html', context=data)
