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
        # extended_staff.services.set(extended_staff_profile_form.cleaned_data.get('services'))
        serv_list=request.POST.get('service_list')
        serv_list=serv_list[:-1]
        print(serv_list)
        s_list = serv_list.split(", ")
        print(s_list)
        for s in s_list:
            s2 = Service.objects.get(servicename=s)
            extended_staff.services.add(s2.id)
        extended_staff.save()
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
            obj.services.set("")
            for field in ['about', 'phone_number','is_active']:
                setattr(obj, field,
                        model_form.cleaned_data.get(field))
            for s in s_list:
                s2 = Service.objects.get(servicename=s)
                obj.services.add(s2.id)
            obj.save()
            return redirect('/staff/')
        else:
            model_form = StaffUpdateForm()
    context = {
        'form': model_form,
        'object': obj,
        's_obj': s_obj
    }
    return render(request, 'edit_staff.html', context)


class StaffListView(ListView):
    model = StaffModel
    template_name = 'staff_list.html'
    queryset = StaffModel.objects.all()
