from django.shortcuts import render, redirect
from .models import Resident, Address, House, Family, LocalBusiness, IDCard, KebeleHouse, KebeleLand
from .forms import ResidentForm, LocalBusinessForm, AddressForm
from django.contrib import messages
# Create your views here.

def home(request):
    
    return render(request, 'kebele/home.html')

##############
# managing resident
#
def manage_resident(request):
    residents = Resident.objects.all()
    addresses = Address.objects.all()
    context={'residents':residents, 'addresses':addresses}
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
    

def update_resident(request, id):
    resident = Resident.objects.get(pk=id)    
    form = ResidentForm(instance=resident)
    if request.method == "POST":
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected resident')
            return redirect('home')
        else:
             messages.warning(request, 'There was an error while updating the resident, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)


# address crud
def add_address(request, id):
    resident = Resident.objects.get(pk=id) 
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():

            addr = form.save(commit=False)
            Address.resident = resident
            addr.save()
            messages.success(request, 'You have successfully added local business')
            return redirect('home')
        else:
            messages.error(request, 'Error occurred') 
    context={'form':form} 
    return render(request, "kebele/form.html", context)


def update_address(request, id):
    address = Address.objects.get(pk=id)    
    form = AddressForm(instance=address)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected address')
            return redirect('home')
        else:
             messages.warning(request, 'There was an error while updating the address, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)


# ?end of managing resident
###############


##############
# managing vital data
#
def manage_vital_data(request):
    context={}
    return render(request, 'kebele/manage_vital_data.html', context)



##############
# managing local business
#
def manage_local_business(request):
    local_business = LocalBusiness.objects.all()
    context={'local_business':local_business}
    return render(request, 'kebele/manage_local_business.html', context)

def add_local_business(request):
    form = LocalBusinessForm()
    if request.method == 'POST':
        form = LocalBusinessForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added local business')
            return redirect('home')  
        else:
            messages.warning(request, 'There was an error while adding the local business, please try again later!')
             
    context={'form':form} 
    return render(request, "kebele/form.html", context)


def update_local_business(request, id):
    local_business = LocalBusiness.objects.get(pk=id)    
    form = LocalBusinessForm(instance=local_business)
    if request.method == "POST":
        form = LocalBusinessForm(request.POST, instance=local_business)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected local business')
            return redirect('home')
        else:
             messages.warning(request, 'There was an error while updating the local business, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)


def delete_local_business(request, id):
    local_business = LocalBusiness.objects.get(pk=id)
    
    if request.method == "POST":
        if local_business.delete():
            messages.success(request, 'You have successfully deleted the selected local business') 
            return redirect('home')
        else:
            messages.warning(request, 'There was an error during deletion of the selected local business')
    context = {'object': local_business}
    return render(request, 'kebele/delete.html', context)


##############
# managing kebele land
#
def manage_kebele_land(request):
    context={}
    return render(request, 'kebele/manage_kebele_land.html', context)

def manage_kebele_house(request):
    context={}
    return render(request, 'kebele/manage_kebele_house.html', context)

