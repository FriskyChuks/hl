from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from cars.models import Car, CarOwnerDriverRegister, BankAccountInformation

from .forms import LoginForm, SignUpForm


@login_required(login_url="/login/")
def home_view(request):
    cars = Car.objects.all()

    template = 'dashboard.html'
    context = {"cars":cars}
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

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)

            messages.success(request, "User created successfully! - please login to continue")
            
            return redirect("/login")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "account/register.html", {"form": form, "msg" : msg, "success" : success })


@login_required
def account_setting_view(request, user_id):
    user = User.objects.get(id=user_id)
    template = 'account/setting.html'
    context = {"user":user}
    return render(request, template, context)


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'account/passwords/change.html'
    success_url = reverse_lazy('password_change_done')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/passwords/reset_done.html'


def logout_view(request):
    logout(request)
    # messages.success(request, "Sad to see you leave! See you soon please!")
    return HttpResponseRedirect('%s'%(reverse("home")))
