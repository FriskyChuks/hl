from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import User

from .models import BankAccountInformation, DriverRequest#, SitBackAndEarn
from .forms import CarOwnersDriversForm#, SitBackAndEarnForm


@login_required
def car_owners_and_drivers_view(request):
    user = request.user

    form = CarOwnersDriversForm(request.POST or None)
    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.user_id = request.user.id
        form_obj.save()
        return redirect("bank_account_info", user_id=user.id)
    
    template = 'drivers/owners_drivers.html'
    context = {"form":form}
    return render(request, template, context)


@login_required
def bank_account_info_view(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        account_name = request.POST.get('account_name')
        account_type = request.POST.get('account_type')
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        form_obj = BankAccountInformation.objects.create(
            user_id = user_id,
            account_name = account_name,
            bank_name = bank_name,
            account_type = account_type,
            account_number = account_number
        )
        form_obj.save()
        messages.success(request, 'Thanks for updating your details; you can continue with other things')
        return redirect("/")
    
    return render(request, 'drivers/bank_account_info.html', {"user":user})


@login_required
def driver_request_view(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        valid_licence = request.POST.get('valid_licence')
        licence_issue_date=request.POST.get('licence_issue_date')
        licence_exp_date = request.POST.get('licence_exp_date')
        licence_no = request.POST.get('licence_no')
        comments = request.POST.get('comments')
        form_obj = DriverRequest.objects.create(
            user_id = user_id,
            valid_licence = valid_licence,
            licence_issue_date=licence_issue_date,
            licence_exp_date = licence_exp_date,
            licence_no=licence_no,
            comments = comments
        )
        form_obj.save()
        messages.success(request, 'Thanks for you request, we shall contact you soon!')
        return redirect("/")
    
    return render(request, 'drivers/driver_request.html', {"user":user})


# @login_required
# def sit_back_and_earn_view(request):
#     form = SitBackAndEarnForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form_obj = form.save(commit=False)
#         form_obj.user=request.user
#         form_obj.save()
#         messages.success(request, 'Thanks for you request, we shall contact you soon!')
#         return redirect("/")
    
#     return render(request, 'drivers/sit_back_n_earn.html', {"form":form})


@login_required
def pending_drivers_request_view(request):
    pending_requests = DriverRequest.objects.filter(status='pending') | DriverRequest.objects.filter(status='interview')

    template = 'drivers/pending_drivers_request.html'
    context = {"pending_requests":pending_requests}
    return render(request, template, context)


@login_required
def drivers_request_detail_view(request, id):
    obj = DriverRequest.objects.get(id=id)
    if request.method == 'POST':
        if obj.status == 'pending':
            obj_update = DriverRequest.objects.filter(id=id).update(status='interview')
            return redirect('pending_driver_request')
        else:
            obj_update = DriverRequest.objects.filter(id=id).update(status='approved')
            driver_id = obj.user.id
            user_updated = User.objects.filter(id=driver_id).update(is_a_driver=True)
            return redirect('pending_driver_request')

    template = 'drivers/driver_request_detail.html'
    context = {"obj":obj}
    return render(request, template, context)
