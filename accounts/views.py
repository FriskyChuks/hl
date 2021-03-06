from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from riders.models import ServiceType
from driver.models import CarOwnerDriverRegister, BankAccountInformation
from cars.models import Car

from .models import User
from .forms import LoginForm, SignUpForm


def home_view(request):
    cars = Car.objects.all()
    services = ServiceType.objects.filter(active=True)

    template = 'dashboard.html'
    context = {"cars":cars, "services":services}
    return render(request, template, context)


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            
            if user is not None:
                login(request, user)
                is_driver = user.is_a_driver
                is_car_owner = user.is_car_owner
                car_owner_driver_profile = CarOwnerDriverRegister.objects.filter(user_id=user.id)
                has_bank_info = BankAccountInformation.objects.filter(user_id=user.id)
                if (is_driver or is_car_owner):
                    if (len(car_owner_driver_profile) <= 0):
                        messages.info(request, 'Kindly update your record before proceeding, thanks!')
                        return redirect("/cars/car_owners_and_drivers")
                    elif not has_bank_info:
                        messages.info(request, "Kindly update your bank details before proceeding, thanks!")
                        return redirect("bank_account_info", user_id=user.id)
                    else:
                        if "next" in request.POST:
                            messages.info(request, 'Please login to continue')
                            return redirect(request.POST.get('next'))
                        else:
                            return redirect("/")
                else:
                    if "next" in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect("/")
            else:    
                msg = 'Not Ok' 

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)   
        qs = User.objects.filter(email=email)
        if len(qs) < 1:
            msg = 'This User does not exist!'
        
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        if user is not None and not user.check_password(password):
            msg = 'Wrong Password'
        elif user is None:
            pass    

    return render(request, "account/login.html", {"form": form, "msg" : msg})



def register_user(request):
    msg  = None
    msg1 = ""
    msg2 = ""
    msg3 = ""
    msg4 = ""

    if request.method == "POST":
        email = request.POST.get("email")
        qs = User.objects.filter(email=email)
        if len(qs) == 1:
            msg = 'This "EMAIL" has already been assigned to a user'
        else:
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get("email")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(email=email, password=raw_password)

                messages.success(request, "User created successfully! - please login to continue")
                
                return redirect("/login")

            else:
                raw_password = form.cleaned_data.get("password1")
                raw_password2 = form.cleaned_data.get("password2")
                if raw_password != raw_password2:
                    msg = 'Passwords do not match' 
                if len(raw_password) < 8:
                    msg = 'password lenght must be greater than 7' 
                    msg1 = 'Length must be greater than 7'
                    msg2 = 'Do not use the word "PASSWORD"'
                    msg3 = 'Do not use your names for password'
                    msg4 = 'Do not use NUMBERS (0-9) alone'   
    else:
        form = SignUpForm()

    context = {"form": form, "msg" : msg, "msg1" : msg1, "msg2":msg2, "msg3":msg3, "msg4":msg4 }
    return render(request, "account/register.html", context)


@login_required
def account_setting_view(request, user_id):
    user = User.objects.get(id=user_id)
    template = 'account/setting.html'
    context = {"user":user}
    return render(request, template, context)


# class MyPasswordChangeView(PasswordChangeView):
#     template_name = 'account/passwords/change.html'
#     success_url = reverse_lazy('password_change_done')

# class MyPasswordResetDoneView(PasswordResetDoneView):
#     template_name = 'account/passwords/reset_done.html'

def logout_view(request):
    logout(request)
    # messages.success(request, "Sad to see you leave! See you soon please!")
    return HttpResponseRedirect('%s'%(reverse("home")))
