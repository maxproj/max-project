from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Infodate
from .forms import InfodateForm

def index(request):
    #	primer1 = Infodate.objects.all().filter(conder = 'нет')
    return render(request, 'Infodate/index.html', {})


def calcul(request):
    calculat = Infodate.objects.all().filter(conder='да')
    return render(request, 'Infodate/calcul.html', {'calculat': calculat})


def engine(request):
    return render(request, 'Infodate/engine.html', {})

def input_new(request):
    if request.method == "POST":
        form = InfodateForm(request.POST)
        if form.is_valid():
            infodate = form.save(commit=False)
            infodate.author = request.user
            infodate.date_publish = timezone.now()
            infodate.save()
            return calcul(request)
#            return redirect('calcul', pk=infodate.pk)
    else:
        form = InfodateForm()
    return render(request, 'Infodate/input_edit.html', {'form': form})


#	def index(request):
#	infodates = Infodate.objects.all().filter(conder = 'нет')
#	return render(request, 'Infodate/index.html',{'infodates': infodates})


# def primer(request):
#    primer1 = Infodate.objects.all().order_by('date_publish')
# 	return render(request, 'Infodate/primer.html',{'primer1':primer1})
# Create your views here.
