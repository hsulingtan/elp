from django.shortcuts import render
#from django.http import HttpResponse
#from elpapp.models import Employer,jobs,AccessRecord,Student
#you don't need the above anymore because we are importing the forms instead
from elpapp.forms import NewStudentform, NewEmployerform, EUserProfileInfoform, SUserProfileInfoform, EUserForm, SUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'elpapp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in")

def Cemployer(request):
    return render(request, 'elpapp/employer.html')

def Cstudent(request):
    return render(request, 'elpapp/student.html')

def eregister(request):
    registered = False
    if request.method == "POST":
        euser_form = EUserForm(data=request.POST)
        eprofile_form = EUserProfileInfoform(data=request.POST)

        if euser_form.is_valid() and eprofile_form.is_valid():
            euser = euser_form.save()
            euser.set_password(euser.password)
            euser.save()

            eprofile = eprofile_form.save(commit = False)
            eprofile.euser = euser

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            eprofile.save()
            registered = True

        else:
            print(euser_form.errors,eprofile_form.errors)
    else:
        euser_form = EUserForm()
        eprofile_form = EUserProfileInfoform()

    return render(request,'elpapp/eregister.html',{'euser_form':euser_form,'eprofile_form':eprofile_form,'registered':registered})

def sregister(request):
    registered = False
    if request.method == "POST":
        suser_form = SUserForm(data=request.POST)
        sprofile_form = SUserProfileInfoform(data=request.POST)

        if suser_form.is_valid() and sprofile_form.is_valid():
            suser = suser_form.save()
            suser.set_password(suser.password)
            suser.save()

            sprofile = sprofile_form.save(commit = False)
            sprofile.suser = suser

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            sprofile.save()
            registered = True

        else:
            print(suser_form.errors,sprofile_form.errors)
    else:
        suser_form = SUserForm()
        sprofile_form = SUserProfileInfoform()

    return render(request,'elpapp/sregister.html',{'suser_form':suser_form,'sprofile_form':sprofile_form,'registered':registered})

#def register(request):
#    registered = False
#    if request.method == "POST":
#        user_form = UserForm(data=request.POST)
#        profile_form = UserProfileInfoform(data=request.POST)

#        if user_form.is_valid() and profile_form.is_valid():
#            user = user_form.save()
#            user.set_password(user.password)
#            user.save()

#            profile = profile_form.save(commit = False)
#            profile.user = user

#            if 'profile_pic' in request.FILES:
#                profile.profile_pic = request.FILES['profile_pic']

#            profile.save()
#            registered = True

#        else:
#            print(user_form.errors,profile_form.errors)
#    else:
#        user_form = UserForm()
#        profile_form = UserProfileInfoform()

#    return render(request,'elpapp/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'elpapp/login.html',{})

def Employer(request):
    form = NewEmployerform()
    if request.method == "POST":
        form = NewEmployerform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'elpapp/eform_page.html',{'form':form})

def Student(request):
    form = NewStudentform()
    if request.method == 'POST':
        form = NewStudentform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'elpapp/sform_page.html',{'form':form})
