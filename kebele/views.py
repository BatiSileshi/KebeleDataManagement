from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Resident, Address, House, Family, LocalBusiness, IDCard, BusinessOwner, KebeleHouse, Kebele, BirthCertificate
from employee.models import Employee
from .forms import ResidentForm, LocalBusinessForm, AddressForm, HouseForm, FamilyForm, IDCardForm, KebeleHouseForm, BusinessOwnerForm, BirthCertificateForm
from django.contrib import messages
# Create your views here.
from django.contrib.gis.geos import Point


@login_required(login_url='login')
def home(request):
    profile = request.user.profile
    count_resident = Resident.objects.all().count()
    count_employee = Employee.objects.all().count()
    count_lb = LocalBusiness.objects.all().count()
    count_kh = KebeleHouse.objects.all().count()
    kebele = Kebele.objects.all()
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponseRedirect("index")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context ={'count_resident':count_resident, 'count_employee':count_employee, 'count_lb':count_lb, 'count_kh':count_kh, 'unreadCount':unreadCount, 'kebele':kebele}
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
        return HttpResponse("handler404")
    
    residents = Resident.objects.all()
    addresses = Address.objects.all()
    houses = House.objects.all()
    families = Family.objects.all()
    idcards = IDCard.objects.all()
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context={'residents':residents, 'addresses':addresses, 'houses':houses, 'families':families, 'idcards':idcards, 'unreadCount':unreadCount}
    return render(request, 'kebele/manage_resident.html', context)





@login_required(login_url='login')
def add_resident(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("handler404")
    form = ResidentForm()
    if request.method == 'POST':
        form = ResidentForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            messages.success(request, 'You have successfully added resident')
            return redirect('manage-resident') 
        else:
            messages.warning(request,'There was an error during registration of resident')
        
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()  
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "kebele/resident_form.html", context)
    

@login_required(login_url='login')
def update_resident(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        resident = Resident.objects.get(pk=id)   
    except:
        return HttpResponse("handler404")
     
    form = ResidentForm(instance=resident)
    if request.method == "POST":
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected resident')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the resident, please try again later!')
             
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'form': form, 'unreadCount': unreadCount}
    return render(request, 'kebele/resident_form.html', context)


def view_resident(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        resident = Resident.objects.get(pk=id)   
    except:
        return HttpResponse("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'resident': resident, 'unreadCount': unreadCount}
    return render(request, 'kebele/view_resident.html', context)


# address crud
@login_required(login_url='login')
def add_address(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        resident = Resident.objects.get(pk=id)    
    except:
        return HttpResponseRedirect("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    
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
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "kebele/address_form.html", context)


@login_required(login_url='login')
def update_address(request, id):
 
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        address = Address.objects.get(pk=id) 
    except:
        return HttpResponse("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
  
    form = AddressForm(instance=address)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected address')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the address, please try again later!')
    context = {'form': form, 'unreadCount': unreadCount}
    return render(request, 'kebele/address_form.html', context)


# house crud
@login_required(login_url='login')
def add_house(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = HouseForm()
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added house')
            return redirect('manage-resident')
        else:
            messages.error(request, 'Error occurred') 
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "kebele/house_form.html", context)


@login_required(login_url='login')
def update_house(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        house = House.objects.get(pk=id) 
    except:
        return HttpResponse("handler404")
       
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = HouseForm(instance=house)
    if request.method == "POST":
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected house')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the house, please try again later!')
    context = {'form': form, 'unreadCount': unreadCount}
    return render(request, 'kebele/house_form.html', context)


def view_house(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        house = House.objects.get(pk=id)   
    except:
        return HttpResponseRedirect("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'house': house, 'unreadCount': unreadCount}
    return render(request, 'kebele/view_house.html', context)


# family crud
@login_required(login_url='login')
def add_family(request):
    
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = FamilyForm()
    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added family')
            return redirect('manage-resident')
        else:
            messages.error(request, 'Error occurred') 
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "kebele/family_form.html", context)


@login_required(login_url='login')
def update_family(request, id):
      
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        family = Family.objects.get(pk=id) 
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = FamilyForm(instance=family)
    if request.method == "POST":
        form = FamilyForm(request.POST, instance=family)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected family')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the family, please try again later!')
    context = {'form': form, 'unreadCount': unreadCount}
    return render(request, 'kebele/family_form.html', context)


def view_family(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        family = Family.objects.get(pk=id)   
    except:
        return HttpResponseRedirect("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    members = family.members.all()
    family_houses = family.house.all()
    context = {'family': family, 'members':members, 'family_houses':family_houses, 'unreadCount': unreadCount}
    return render(request, 'kebele/view_family.html', context)


 

# IDCArd crud
@login_required(login_url='login')
def add_id_card(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = IDCardForm()
    if request.method == 'POST':
        form = IDCardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added ID Card')
            return redirect('manage-resident')
        else:
            messages.error(request, 'Error occurred') 
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "kebele/id_form.html", context)


@login_required(login_url='login')
def update_id_card(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        card = IDCard.objects.get(pk=id)
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
        
    form = IDCardForm(instance=card)
    if request.method == "POST":
        form = IDCardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected ID Card')
            return redirect('manage-resident')
        else:
             messages.warning(request, 'There was an error while updating the family, please try again later!')
    context = {'form': form, 'unreadCount': unreadCount}
    return render(request, 'kebele/id_form.html', context)




def view_idcard(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        idcard = IDCard.objects.get(pk=id)   
    except:
        return HttpResponseRedirect("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {'idcard': idcard, 'unreadCount': unreadCount}
    return render(request, 'kebele/view_idcard.html', context)

# ?end of managing resident
###############



##############
# managing local business
#
@login_required(login_url='login')
def manage_local_business(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    local_business = LocalBusiness.objects.all()
    business_owners = BusinessOwner.objects.all()
    context={'local_business':local_business, 'business_owners':business_owners, 'unreadCount':unreadCount}
    return render(request, 'kebele/manage_local_business.html', context)

# lb owner crud
@login_required(login_url='login')
def add_lb_owner(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = BusinessOwnerForm()
    if request.method == 'POST':
        form = BusinessOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added local business owner')
            return redirect('manage-local-business')  
        else:
            messages.warning(request, 'There was an error while adding the local business, please try again later!')
             
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "kebele/lb_owner_form.html", context)


@login_required(login_url='login')
def update_lb_owner(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        business_owner = BusinessOwner.objects.get(pk=id) 
    except:
        return HttpResponse("handler404") 
       
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = BusinessOwnerForm(instance=business_owner)
    if request.method == "POST":
        form = BusinessOwnerForm(request.POST, instance=business_owner)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected local business owner')
            return redirect('manage-local-business')
        else:
             messages.warning(request, 'There was an error while updating the local business owner, please try again later!')
    context = {'form': form, 'unreadCount': unreadCount}
    return render(request, 'kebele/lb_owner_form.html', context)


@login_required(login_url='login')
def delete_lb_owner(request, id):
    
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        business_owner = BusinessOwner.objects.get(pk=id) 
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    if request.method == "POST":
        if business_owner.delete():
            messages.success(request, 'You have successfully deleted the selected local business owner') 
            return redirect('manage-local-business')
        else:
            messages.warning(request, 'There was an error during deletion of the selected local business owner')
    context = {'object': business_owner, 'unreadCount': unreadCount}
    return render(request, 'kebele/delete.html', context)

# LB crud
@login_required(login_url='login')
def add_local_business(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = LocalBusinessForm()
    if request.method == 'POST':
        form = LocalBusinessForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added local business')
            return redirect('manage-local-business')  
        else:
            messages.warning(request, 'There was an error while adding the local business, please try again later!')
             
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "kebele/lb_form.html", context)


@login_required(login_url='login')
def update_local_business(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        local_business = LocalBusiness.objects.get(pk=id)  
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
       
    form = LocalBusinessForm(instance=local_business)
    if request.method == "POST":
        form = LocalBusinessForm(request.POST, instance=local_business)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected local business')
            return redirect('manage-local-business')
        else:
             messages.warning(request, 'There was an error while updating the local business, please try again later!')
    context = {'form': form, 'unreadCount': unreadCount}
    return render(request, 'kebele/lb_form.html', context)


@login_required(login_url='login')
def delete_local_business(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        local_business = LocalBusiness.objects.get(pk=id)  
    except:
        return HttpResponse("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    if request.method == "POST":
        if local_business.delete():
            messages.success(request, 'You have successfully deleted the selected local business') 
            return redirect('manage-local-business')
        else:
            messages.warning(request, 'There was an error during deletion of the selected local business')
    context = {'object': local_business, 'unreadCount': unreadCount}
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
        return HttpResponse("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    kebele_houses = KebeleHouse.objects.all()
    context={'kebele_houses':kebele_houses, 'unreadCount':unreadCount}
    return render(request, 'kebele/manage_kebele_house.html', context)

@login_required(login_url='login')
def add_kebele_house(request):
    profile = request.user.profile
    residents = {}
    try:
      Employee.objects.get(employee=profile)
      resident_ids = list(KebeleHouse.objects.all().values_list('resident',flat=True).distinct())
      residents =  Resident.objects.all().exclude(id__in=resident_ids)
    except:
        return HttpResponse("handler404")
   
    if request.method == 'POST':
            #code for adding kebele house 
            hnum = request.POST.get("hnum")
            door_number = request.POST.get("door_number")
            area = request.POST.get("area")
            resident = request.POST.get("resident")
            lat = float(request.POST.get('lat'))
            lng = float(request.POST.get('lng'))
            location = Point(lng, lat,srid=4326)
            
            try:
                resident = Resident.objects.get(id=resident)
            except:
                resident = None
                
            
            house = KebeleHouse.objects.create(hnum=hnum, door_number=door_number,area = area,location=location)
            if resident != None:
                house.resident = resident
                house.save()
            else:
                house.resident = None
                house.save()
            messages.success(request, 'You have successfully added kebele house')
            return redirect('manage-kebele-house')  
        # else:
        #     messages.warning(request, 'There was an error while adding kebele house, please try again later!')
             
    context={'residents':residents} 
    return render(request, "kebele/add_kebele_house.html", context)


@login_required(login_url='login')
def update_kebele_house(request, id):
    profile = request.user.profile
    residents = []
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        kebele_house = KebeleHouse.objects.get(pk=id) 
        resident_ids = list(KebeleHouse.objects.all().values_list('resident',flat=True).distinct())
        residents =  Resident.objects.all().exclude(id__in=resident_ids)
    except:
        return HttpResponse("handler404")   
  
    if request.method == "POST":
            hnum = request.POST.get("hnum")
            door_number = request.POST.get("door_number")
            area = request.POST.get("area")
            resident = request.POST.get("resident")
            lat = float(request.POST.get('lat'))
            lng = float(request.POST.get('lng'))
            location = Point(lng, lat,srid=4326)
            
            try:
                resident = Resident.objects.get(id=resident)
            except:
                resident = None
                
            
            kebele_house.area = area
            kebele_house.hnum = hnum
            kebele_house.location = location
            kebele_house.door_number = door_number
            kebele_house.save()
            if resident != None:
                kebele_house.resident = resident
                kebele_house.save()
            else:
                kebele_house.resident = None
                kebele_house.save()
            messages.success(request, 'You have successfully updated the selected kebele house')
            return redirect('manage-kebele-house')

    context = {'kebele_house':kebele_house,'residents':residents}
    return render(request, 'kebele/update_kebele_house.html', context)


def view_kebele_house(request, id):
    try:
        kebele_house = KebeleHouse.objects.get(id=id) 
    except:
        return HttpResponseRedirect("handler404")
    context = {'kebele_house': kebele_house}
    return render(request, 'kebele/view_kebele_house.html', context)




@login_required(login_url='login')
def see_map(request):
    kebele_houses = KebeleHouse.objects.all()
    context={'kebele_houses':kebele_houses}
    return render(request, 'kebele/see_map.html', context)


@login_required(login_url='login')
def see_house_in_map(request,pk):
    try:

        kebele_house= KebeleHouse.objects.get(id=pk)
    except:
        return  HttpResponseRedirect('handler404')

    context={'kebele_house':kebele_house}
    return render(request, 'kebele/see_house_in_map.html', context)



#
# ?end of managing kebele house
####################################



##########################

def certificates(request):
    certificates = BirthCertificate.objects.all()
    context={'certificates':certificates}
    return render(request, 'kebele/certificates.html', context)


login_required(login_url='login')
def add_birth_certificate(request):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
    except:
        return HttpResponse("handler404")
    form = BirthCertificateForm()
    if request.method == 'POST':
        form = BirthCertificateForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            messages.success(request, 'You have successfully added birth')
            return redirect('certificates') 
        else:
            messages.warning(request,'There was an error during registration of birth certificate')
        
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()  
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "kebele/birth_form.html", context)
    

# @login_required(login_url='login')
# def update_birth_certificate(request, id):
#     profile = request.user.profile
#     try:
#         kebele_employee = Employee.objects.get(employee=profile)
#         certificate = BirthCertificate.objects.get(pk=id)   
#     except:
#         return HttpResponse("handler404")
     
#     form = BirthCertificateForm(instance=certificate)
#     if request.method == "POST":
#         form = BirthCertificateForm(request.POST, instance=certificate)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'You have successfully updated the selected certificate')
#             return redirect('certificates')
#         else:
#              messages.warning(request, 'There was an error while updating the certificate, please try again later!')
             
#     messageRequests = kebele_employee.messages.all()
#     unreadCount = messageRequests.filter(is_read=False).count()
#     context = {'form': form, 'unreadCount': unreadCount}
#     return render(request, 'kebele/birth_form.html', context)


def view_birth_certificate(request, id):
    profile = request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)
        birth = BirthCertificate.objects.get(pk=id)   
    except:
        return HttpResponse("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'birth': birth, 'unreadCount': unreadCount}
    return render(request, 'kebele/view_birth_certificate.html', context)