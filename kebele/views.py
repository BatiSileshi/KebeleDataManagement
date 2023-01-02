from django.shortcuts import render, redirect
from .models import Resident, Address, House, Family, LocalBusiness, IDCard, KebeleHouse, KebeleLand
from .forms import ResidentForm
# Create your views here.

def home(request):
    
    return render(request, 'kebele/home.html')

##############
# managing resident
#
def manage_resident(request):
    residents = Resident.objects.all()
    context={'residents':residents}
    return render(request, 'kebele/manage_resident.html', context)


def add_resident(request):
    form = ResidentForm()
    if request.method == 'POST':
        form = ResidentForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('home')   
    context={'form':form} 
    return render(request, "kebele/form.html", context)
    


def manage_vital_data(request):
    context={}
    return render(request, 'kebele/manage_vital_data.html', context)

def manage_local_business(request):
    context={}
    return render(request, 'kebele/manage_local_business.html', context)

def manage_kebele_land(request):
    context={}
    return render(request, 'kebele/manage_kebele_land.html', context)

def manage_kebele_house(request):
    context={}
    return render(request, 'kebele/manage_kebele_house.html', context)

