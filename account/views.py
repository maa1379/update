from django.shortcuts import render, redirect
from .forms import SpecialUserForm, LoginForm
from django.views.generic import FormView, ListView
from .models import User, Profile
from django.urls import reverse_lazy
from .mixins import AdminUserAccess
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import Http404


# special user

class SpecialUserCrateView(AdminUserAccess, FormView):
    form_class = SpecialUserForm
    template_name = "account/special_user_create.html"
    success_url = reverse_lazy("config:panel_home")

    def form_valid(self, form):
        cd = form.cleaned_data
        user = User.objects.create_user(email=cd["email"], password=cd["password"])
        user.profile.first_name = cd["first_name"]
        user.profile.last_name = cd["last_name"]
        user.profile.company_name = cd["company"]
        user.profile.phone_number = cd["phone_number"]
        user.profile.position = cd["position"]
        user.profile.description = cd["description"]
        user.is_patient_user = True
        user.profile.save()
        return super(SpecialUserCrateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, "btn-danger")
        return super(SpecialUserCrateView, self).form_invalid(form)


class SpecialUserList(ListView):
    queryset = User.objects.filter(is_special_user=True)
    template_name = "account/special_user_list.html"


# patient user

class PatientUserList(ListView):
    queryset = User.objects.filter(is_patient_user=True)
    template_name = "account/patient_user_list.html"


# user login
class LoginView(FormView):
    form_class = LoginForm
    template_name = "account/login.html"
    success_url = reverse_lazy("config:site_home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404()
        return super(LoginView, self).dispatch(request, *args, *kwargs)

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(email=cd["email"], password=["password"])
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "user logged in", "btn-success")
            return redirect("config:site_home")
        messages.error(self.request, "authentication failed", "btn-danger")
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, "btn-danger")
        return super(LoginView, self).form_invalid(form)
