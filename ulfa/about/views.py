from django.shortcuts import render

from .models import habib

def iklil(request):
    yuhu = habib.objects.all()
    context = {
        'ygy' : yuhu ,

    }
    return render(request,'tahu.html',context)
