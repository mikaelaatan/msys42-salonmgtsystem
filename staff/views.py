from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StaffModelForm, ExtendedStaffModelForm, StaffUpdateForm
from .models import StaffModel
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.views.generic import *
from django.urls import reverse


#============= SIGN UP STAFF ==================
def signup_staff_view(request):
    staff_profile_form = StaffModelForm(request.POST or None, request.FILES or None)
    extended_staff_profile_form = ExtendedStaffModelForm(request.POST or None, request.FILES or None)
    valid = staff_profile_form.is_valid() * extended_staff_profile_form.is_valid()
    if valid:
        staff = staff_profile_form.save()
        group = Group.objects.get(name='Staff')
        staff.groups.add(group)
        extended_staff = StaffModel.objects.create(user=staff)
        for field in ['about', 'phone_number']:
            setattr(extended_staff, field,
                    extended_staff_profile_form.cleaned_data.get(field))
        extended_staff.services.set(extended_staff_profile_form.cleaned_data.get('services'))
        extended_staff.save()
        return redirect('/staff/')
    context = {
        'profile_form': staff_profile_form,
        'extended_profile_form': extended_staff_profile_form,
    }
    return render(request, 'registration/login.html', context)

#=============== DELETE VIEW ====================
### there's no delete. instead the admin can deactivate a user. ###

#=============== DETAILED VIEW ==================
def dynamic_lookup_view(request,id):
    obj = get_object_or_404(StaffModel, id=id)
    context = {
        "object": obj
    }
    return render(request, "staff_detail.html", context)

def create_staff(request):
    return render(request, 'createstaff.html')

class StaffListView(ListView):
    model = StaffModel
    template_name = 'staff_list.html'
    queryset = StaffModel.objects.all()

class StaffUpdateView(UpdateView):
    template_name = 'editstaff.html'
    form_class = StaffUpdateForm
    queryset = StaffModel.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(StaffModel, id=id_)

    # def service_details(request):
    #     # selected_service = Service.objects.get(id=id)
    #     selected_service = request.GET['selected_service']
    #     return get_object_or_404(Service, pk=selected_service)

    def service_list(request):
        selected_service = Service.objects.all()
        context = {
            "s_service": selected_service
        }
        return render(request, context)



# class StaffCreateView(CreateView):
#     template_name = 'addstaff.html'
#     form_class = StaffModelForm
#     queryset = StaffModel.objects.all()
#
# class ServiceDeleteView(DeleteView):
#     template_name = 'deletestaff.html'
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Staff, id=id_)
#
#     def get_success_url(self):
#         return reverse('staff:staff-list')
