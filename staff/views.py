from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import StaffModelForm, ExtendedStaffModelForm, StaffUpdateForm
from .models import StaffModel
from services.models import Service
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.views.generic import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from decorators import user_required, staff_required, admin_required
from django.utils.decorators import method_decorator
from django.contrib import messages


#============= SIGN UP STAFF ==================
@admin_required
def signup_staff_view(request):
    s_obj = Service.objects.all()
    staff_profile_form = StaffModelForm(request.POST or None, request.FILES or None)
    extended_staff_profile_form = StaffUpdateForm(request.POST or None, request.FILES or None)
    valid = staff_profile_form.is_valid() * extended_staff_profile_form.is_valid()
    if valid:
        staff = staff_profile_form.save()
        group = Group.objects.get(name='Staff')
        staff.groups.add(group)
        extended_staff = StaffModel.objects.create(user=staff)
        for field in ['about', 'phone_number','is_active']:
            setattr(extended_staff, field,
                    extended_staff_profile_form.cleaned_data.get(field))
        # extended_staff.service.set(extended_staff_profile_form.cleaned_data.get('service'))
        serv_list=request.POST.get('service_list')
        serv_list=serv_list[:-1]
        print(serv_list)
        s_list = serv_list.split(", ")
        print(s_list)
        for s in s_list:
            s2 = Service.objects.get(servicename=s)
            extended_staff.service.add(s2.id)
        extended_staff.save()
        messages.info(request, 'New staff record has been saved successfully!')
        return redirect('/staff/')
    context = {
        'profile_form': staff_profile_form,
        'extended_profile_form': extended_staff_profile_form,
        's_obj': s_obj,
    }
    return render(request, 'registration/register.html', context)

def add_staff_view(request):
    s_obj = Service.objects.all()
    staff_profile_form = StaffModelForm(request.POST or None, request.FILES or None)
    extended_staff_profile_form = StaffUpdateForm(request.POST or None, request.FILES or None)
    valid = staff_profile_form.is_valid() * extended_staff_profile_form.is_valid()
    if valid:
        staff = staff_profile_form.save()
        group = Group.objects.get(name='Staff')
        staff.groups.add(group)
        extended_staff = StaffModel.objects.create(user=staff)
        for field in ['about', 'phone_number','is_active']:
            setattr(extended_staff, field,
                    extended_staff_profile_form.cleaned_data.get(field))
        # extended_staff.service.set(extended_staff_profile_form.cleaned_data.get('service'))
        serv_list=request.POST.get('service_list')
        serv_list=serv_list[:-1]
        print(serv_list)
        s_list = serv_list.split(", ")
        print(s_list)
        for s in s_list:
            s2 = Service.objects.get(servicename=s)
            extended_staff.service.add(s2.id)
        extended_staff.save()
        messages.info(request, 'New staff record has been saved successfully!')
        return redirect('/staff/')
    context = {
        'profile_form': staff_profile_form,
        'extended_profile_form': extended_staff_profile_form,
        's_obj': s_obj,
    }
    return render(request, 'create_staff.html', context)

#=============== DETAILED VIEW ==================
def dynamic_lookup_view(request,id):
    obj = get_object_or_404(StaffModel, id=id)
    context = {
        "object": obj
    }
    return render(request, "staff_detail.html", context)

@admin_required
def edit_staff_view(request, id):
    obj = StaffModel.objects.get(id=id)
    print(obj.id)
    s_obj = Service.objects.all()
    model_form = StaffUpdateForm(request.POST or None, request.FILES or None)
    if request.method=="POST":
        if model_form.is_valid():
            serv_list=request.POST.get('service_list')
            print(serv_list)
            if serv_list[-1] == " ":
                serv_list=serv_list[:-1]
            serv_list=serv_list[:-1]
            print(serv_list + "end")
            s_list = serv_list.split(", ")
            print(s_list)
            obj.service.set("")
            for field in ['about', 'phone_number','is_active']:
                setattr(obj, field,
                        model_form.cleaned_data.get(field))
            for s in s_list:
                s2 = Service.objects.get(servicename=s)
                obj.service.add(s2.id)
            obj.save()
            messages.info(request, 'Staff has been edited successfully!')
            return redirect('/staff/'+str(obj.id))
        else:
            model_form = StaffUpdateForm()
    context = {
        'form': model_form,
        'object': obj,
        's_obj': s_obj
    }
    return render(request, 'edit_staff.html', context)

def stafflist_view(request):
    if hasattr(request.user, 'user'):
        staff = StaffModel.objects.filter(is_active=True)
    else:
        staff = StaffModel.objects.all()
    staff_now = staff.order_by('user_id')
    context = {
        'object_list': staff_now,
    }
    return render(request, 'staff_list.html', context)
