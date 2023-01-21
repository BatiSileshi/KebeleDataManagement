from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Resident, Address, House, Family, LocalBusiness, IDCard, BusinessOwner, KebeleHouse, KebeleLand
from employee.models import Employee
from .forms import ResidentForm, LocalBusinessForm, AddressForm, HouseForm, FamilyForm, IDCardForm, KebeleLandForm, KebeleHouseForm, BusinessOwnerForm
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def home(request):
    profile = request.user.profile
    count_resident = Resident.objects.all().count()
    count_employee = Employee.objects.all().count()
    count_lb = LocalBusiness.objects.all().count()
    count_kh = KebeleHouse.objects.all().count()
    
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponseRedirect("handler404")
    
    context ={'count_resident':count_resident, 'count_employee':count_employee, 'count_lb':count_lb, 'count_kh':count_kh}
    return render(request, 'kebele/home.html', context)

##############
# managing resident
#
@login_required(login_url='login')
def manage_resident(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here")
    
    residents = Resident.objects.all()
    addresses = Address.objects.all()
    houses = House.objects.all()
    families = Family.objects.all()
    idcards = IDCard.objects.all()
    context={'residents':residents, 'addresses':addresses, 'houses':houses, 'families':families, 'idcards':idcards}
    return render(request, 'kebele/manage_resident.html', context)


@login_required(login_url='login')
def add_resident(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!")
    form = ResidentForm()
    if request.method == 'POST':
        form = ResidentForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('manage-resident')   
    context={'form':form} 
    return render(request, "kebele/form.html", context)
    

@login_required(login_url='login')
def update_resident(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        resident = Resident.objects.get(pk=id)   
    except:
        return HttpResponse("You are not allowed here!")
     
    form = ResidentForm(instance=resident)
    if request.method == "POST":
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected resident')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the resident, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)


def view_resident(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        resident = Resident.objects.get(pk=id)   
    except:
        return HttpResponse("You are not allowed here!")
    context = {'resident': resident}
    return render(request, 'kebele/view_resident.html', context)


# address crud
@login_required(login_url='login')
def add_address(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        resident = Resident.objects.get(pk=id) 
        
    except:
        return HttpResponse("You are not allowed here!")
    
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():

            addr = form.save(commit=False)
            addr.resident = resident
            addr.save()
            messages.success(request, 'You have successfully added local business')
            return redirect('manage-resident')
        else:
            messages.error(request, 'Error occurred') 
            
    # if resident.address:
    #     return HttpResponseRedirect("handler404")
    context={'form':form} 
    return render(request, "kebele/form.html", context)


@login_required(login_url='login')
def update_address(request, id):
 
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        address = Address.objects.get(pk=id) 
    except:
        return HttpResponse("You are not allowed here!")
  
    form = AddressForm(instance=address)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected address')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the address, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)


# house crud
@login_required(login_url='login')
def add_house(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!")
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


@login_required(login_url='login')
def update_house(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        house = House.objects.get(pk=id) 
    except:
        return HttpResponse("You are not allowed here!")
       
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
@login_required(login_url='login')
def add_family(request):
    
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!")
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


@login_required(login_url='login')
def update_family(request, id):
      
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        family = Family.objects.get(pk=id) 
    except:
        return HttpResponse("You are not allowed here!") 
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
@login_required(login_url='login')
def add_id_card(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!") 
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


@login_required(login_url='login')
def update_id_card(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        card = IDCard.objects.get(pk=id)
    except:
        return HttpResponse("You are not allowed here!") 
        
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
@login_required(login_url='login')
def manage_vital_data(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!") 
    
    context={}
    return render(request, 'kebele/manage_vital_data.html', context)



##############
# managing local business
#
@login_required(login_url='login')
def manage_local_business(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!") 
    
    local_business = LocalBusiness.objects.all()
    business_owners = BusinessOwner.objects.all()
    context={'local_business':local_business, 'business_owners':business_owners}
    return render(request, 'kebele/manage_local_business.html', context)

# lb owner crud
@login_required(login_url='login')
def add_lb_owner(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!") 
    
    form = BusinessOwnerForm()
    if request.method == 'POST':
        form = BusinessOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added local business owner')
            return redirect('manage-local-business')  
        else:
            messages.warning(request, 'There was an error while adding the local business, please try again later!')
             
    context={'form':form} 
    return render(request, "kebele/form.html", context)


@login_required(login_url='login')
def update_lb_owner(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        business_owner = BusinessOwner.objects.get(pk=id) 
    except:
        return HttpResponse("You are not allowed here!") 
       
    form = BusinessOwnerForm(instance=business_owner)
    if request.method == "POST":
        form = BusinessOwnerForm(request.POST, instance=business_owner)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected local business owner')
            return redirect('manage-local-business')
        else:
             messages.warning(request, 'There was an error while updating the local business owner, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)


@login_required(login_url='login')
def delete_lb_owner(request, id):
    
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        business_owner = BusinessOwner.objects.get(pk=id) 
    except:
        return HttpResponse("You are not allowed here!") 
    
    if request.method == "POST":
        if business_owner.delete():
            messages.success(request, 'You have successfully deleted the selected local business owner') 
            return redirect('manage-local-business')
        else:
            messages.warning(request, 'There was an error during deletion of the selected local business owner')
    context = {'object': business_owner}
    return render(request, 'kebele/delete.html', context)

# LB crud
@login_required(login_url='login')
def add_local_business(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!") 
    form = LocalBusinessForm()
    if request.method == 'POST':
        form = LocalBusinessForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added local business')
            return redirect('manage-local-business')  
        else:
            messages.warning(request, 'There was an error while adding the local business, please try again later!')
             
    context={'form':form} 
    return render(request, "kebele/form.html", context)


@login_required(login_url='login')
def update_local_business(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        local_business = LocalBusiness.objects.get(pk=id)  
    except:
        return HttpResponse("You are not allowed here!") 
       
    form = LocalBusinessForm(instance=local_business)
    if request.method == "POST":
        form = LocalBusinessForm(request.POST, instance=local_business)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected local business')
            return redirect('manage-local-business')
        else:
             messages.warning(request, 'There was an error while updating the local business, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)


@login_required(login_url='login')
def delete_local_business(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        local_business = LocalBusiness.objects.get(pk=id)  
    except:
        return HttpResponse("You are not allowed here!") 
    
    if request.method == "POST":
        if local_business.delete():
            messages.success(request, 'You have successfully deleted the selected local business') 
            return redirect('manage-local-business')
        else:
            messages.warning(request, 'There was an error during deletion of the selected local business')
    context = {'object': local_business}
    return render(request, 'kebele/delete.html', context)



#############################
# managing kebele house
#
@login_required(login_url='login')
def manage_kebele_house(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile) 
    except:
        return HttpResponse("You are not allowed here!")
    kebele_houses = KebeleHouse.objects.all()
    context={'kebele_houses':kebele_houses}
    return render(request, 'kebele/manage_kebele_house.html', context)

@login_required(login_url='login')
def add_kebele_house(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("You are not allowed here!")
    form = KebeleHouseForm()
    if request.method == 'POST':
        form = KebeleHouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added kebele house')
            return redirect('manage-kebele-house')  
        else:
            messages.warning(request, 'There was an error while adding kebele house, please try again later!')
             
    context={'form':form} 
    return render(request, "kebele/form.html", context)


@login_required(login_url='login')
def update_kebele_house(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        kebele_house = KebeleHouse.objects.get(pk=id)  
    except:
        return HttpResponse("You are not allowed here!")   
    form = KebeleHouseForm(instance=kebele_house)
    if request.method == "POST":
        form = KebeleHouseForm(request.POST, instance=kebele_house)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected kebele house')
            return redirect('manage-kebele-house')
        else:
             messages.warning(request, 'There was an error while updating the kebele land, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)
#
# ?end of managing kebele house
####################################



#############################
# managing kebele land
#
@login_required(login_url='login')
def manage_kebele_land(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile) 
    except:
        return HttpResponse("You are not allowed here!") 
    kebele_lands = KebeleLand.objects.all()
    context={'kebele_lands':kebele_lands}
    return render(request, 'kebele/manage_kebele_land.html', context)


@login_required(login_url='login')
def add_kebele_land(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile) 
    except:
        return HttpResponse("You are not allowed here!") 
    form = KebeleLandForm()
    if request.method == 'POST':
        form = KebeleLandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added kebele land')
            return redirect('manage-kebele-land')  
        else:
            messages.warning(request, 'There was an error while adding kebele land, please try again later!')
             
    context={'form':form} 
    return render(request, "kebele/form.html", context)


@login_required(login_url='login')
def update_kebele_land(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        kebele_land = KebeleLand.objects.get(pk=id)    
    except:
        return HttpResponse("You are not allowed here!") 
      
    form = KebeleLandForm(instance=kebele_land)
    if request.method == "POST":
        form = KebeleLandForm(request.POST, instance=kebele_land)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected kebele land')
            return redirect('manage-kebele-land')
        else:
             messages.warning(request, 'There was an error while updating the kebele land, please try again later!')
    context = {'form': form}
    return render(request, 'kebele/form.html', context)
#
# ?end of managing kebele land
####################################

