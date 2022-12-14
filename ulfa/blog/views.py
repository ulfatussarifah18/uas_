from django.shortcuts import render

from.models import hoby

def fav(request):
    tahu = hoby.objects.all()
    context = {
        'wk': tahu,
    }
    return render(request,'blg.html',context)
