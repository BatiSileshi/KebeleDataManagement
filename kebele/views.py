from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resident, Address, House, Family, LocalBusiness, IDCard, KebeleHouse, KebeleLand
from .forms import ResidentForm, LocalBusinessForm, AddressForm, HouseForm, FamilyForm, IDCardForm
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
    houses = House.objects.all()
    families = Family.objects.all()
    idcards = IDCard.objects.all()
    context={'residents':residents, 'addresses':addresses, 'houses':houses, 'families':families, 'idcards':idcards}
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
            addr.resident = resident
            addr.save()
            messages.success(request, 'You have successfully added local business')
            return redirect('home')
        else:
            messages.error(request, 'Error occurred') 
            
    # if resident.address.resident == resident:
    #     return HttpResponse("teesson dabalame")
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


# house crud
def add_house(request):
    form = HouseForm()
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added house')
            return redirect('manage-resident')
        else:
            messages.error(request, 'Error occurred') 
    context={'form':form} 
    return render(request, "kebele/form.html", context)


def update_house(request, id):
    house = House.objects.get(pk=id)    
    form = HouseForm(instance=house)
    if request.method == "POST":
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected house')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the house, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)

# family crud
def add_family(request):
    form = FamilyForm()
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added family')
            return redirect('manage-resident')
        else:
            messages.error(request, 'Error occurred') 
    context={'form':form} 
    return render(request, "kebele/form.html", context)


def update_family(request, id):
    family = Family.objects.get(pk=id)    
    form = FamilyForm(instance=family)
    if request.method == "POST":
        form = FamilyForm(request.POST, instance=family)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected family')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the family, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)


# IDCArd crud
def add_id_card(request):
    form = IDCardForm()
    if request.method == 'POST':
        form = IDCardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added ID Card')
            return redirect('manage-resident')
        else:
            messages.error(request, 'Error occurred') 
    context={'form':form} 
    return render(request, "kebele/form.html", context)


def update_id_card(request, id):
    card = IDCard.objects.get(pk=id)    
    form = IDCardForm(instance=card)
    if request.method == "POST":
        form = IDCardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected ID Card')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the family, please try again later!')
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

