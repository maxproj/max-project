from django.shortcuts import render

def index(request):
    return render(request, 'Infodate/index.html',{})
# Create your views here.
