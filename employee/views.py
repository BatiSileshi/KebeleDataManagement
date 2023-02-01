from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from.forms import UserCreationForm, KebeleEmployeeForm, ProfileForm, MessageForm
from .models import Employee, Profile, Message
# Create your views here.
 


def index(request):
    
    return render(request, 'employee/index.html')
 


def loginEmployee(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method=='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user=User.objects.get(username=username)
        except: 
            messages.error(request, 'Username does not exist')
            
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home') 
        else:
            messages.error(request, 'Username or password does not exist')
            
    return render(request, 'employee/login_register.html')



def logoutEmployee(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('index')


def registerEmployee(request):   
    page = 'register'
    if request.user.is_authenticated:
        return redirect('index') 
    form= UserCreationForm()
    
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, "Account created!")
            
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Error occurred during registration")
    context={'page':page, 'form':form}
    return render(request, 'employee/login_register.html', context)

@login_required(login_url='login')
def employee_profile(request):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)   
    except:
        return HttpResponseRedirect("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    profile = request.user.profile
    context = {'profile':profile, 'unreadCount':unreadCount}
    return render(request, 'employee/account.html', context)

 
@login_required(login_url='login')
def editProfile(request):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)   
    except:
        return HttpResponseRedirect("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully updated your profile')
            return redirect('account')
        else:
            messages.error(request,'There is an error while processing your in put')
    context = {'form':form, 'unreadCount':unreadCount}
    return render(request, 'employee/form.html',context)


# employee management
@login_required(login_url='login')
def manage_employee(request):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile, role="manager")   
    except:
        return HttpResponseRedirect("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    employees = Employee.objects.all()
    context={'employees':employees, 'unreadCount':unreadCount}
    return render(request, 'employee/manage_employee.html', context)


@login_required(login_url='login')
def add_employee(request):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile, role="manager")   
    except:
        return HttpResponseRedirect("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = KebeleEmployeeForm() 
    if request.method == 'POST':
        form = KebeleEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added employee')
            return redirect('manage-employee')  
        else:
            messages.warning(request, 'There was an error while adding the employee, please try again later!')
             
    context={'form':form, 'unreadCount':unreadCount} 
    return render(request, "employee/form.html", context)


@login_required(login_url='login')
def update_employee(request, id):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile, role="manager")   
        employee = Employee.objects.get(pk=id)  
    except:
        return HttpResponseRedirect("handler404") 
       
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    form = KebeleEmployeeForm(instance=employee)
    if request.method == "POST":
        form = KebeleEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated the selected employee')
            return redirect('manage-employee')
        else:
             messages.warning(request, 'There was an error while updating the employee, please try again later!')
    context = {'form': form, 'unreadCount': unreadCount}
    return render(request, 'employee/form.html', context)

@login_required(login_url='login')
def delete_employee(request, id):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile, role="manager")   
        employee = Employee.objects.get(pk=id)  
    except:
        return HttpResponseRedirect("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    if request.method == "POST":
        if employee.delete():
            messages.success(request, 'You have successfully deleted the selected employee') 
            return redirect('manage-employee')
        else:
            messages.warning(request, 'There was an error during deletion of the selected employee')
    context = {'object': employee, 'unreadCount': unreadCount}
    return render(request, 'employee/delete.html', context)



@login_required(login_url='login')
def inbox(request):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile)   
    except:
        return HttpResponseRedirect("handler404") 
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    sent_messages = Message.objects.filter(sender=kebele_employee)
    sent_messages_count = Message.objects.filter(sender=kebele_employee).count()
    context={'messageRequests':messageRequests, 'unreadCount':unreadCount, 'sent_messages':sent_messages, 'sent_messages_count':sent_messages_count}
    return render(request, 'employee/inbox.html', context)



@login_required(login_url='login')
def view_message(request, pk):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile) 
        message = kebele_employee.messages.get(id=pk)  
    except:
        return HttpResponseRedirect("handler404") 
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    if message.is_read == False:
        message.is_read = True
        message.save()
    context={'message':message, 'unreadCount':unreadCount}
    return render(request, 'employee/message.html', context)


@login_required(login_url='login')
def view_sent_message(request, pk):
    profile=request.user.profile
    try:
        kebele_employee = Employee.objects.get(employee=profile) 
        message = Message.objects.get(id=pk, sender=kebele_employee)  
        recipients = message.recipient.all()
    except:
        return HttpResponseRedirect("handler404") 
     
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context={'message':message, 'unreadCount':unreadCount, 'recipients':recipients}
    return render(request, 'employee/sent_message.html', context)



#  use create method
def create_message_all(request):
    form = MessageForm()
    try: 
        profile = request.user.profile
        kebele_employee = Employee.objects.get(employee=profile)
        sender = kebele_employee
    except:
        return HttpResponseRedirect("handler404")
    
    messageRequests = kebele_employee.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        recip_list = request.POST.getlist("recipient")
        if form.is_valid():
            message = form.save(commit = False)       
            message.sender = sender
            message.save()
            
            for recip in recip_list:
                recipient = {}
                try:
                     recipient = Employee.objects.get(id=recip) 
                except:
                    return HttpResponseRedirect("handler404")   
                message.recipient.add(recipient)  
    
        messages.success(request, 'Your message was successfully sent')
        return redirect('manage-employee')
    
    context={ 'form':form, 'unreadCount':unreadCount}

    return render(request, 'employee/form.html', context) 



def page_not_found(request, exception):
    return render(request, '404.html', status=404)

 
