from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'class': 'form-control'})
        form.fields['password1'].widget.attrs.update({'class': 'form-control'})
        form.fields['password2'].widget.attrs.update({'class': 'form-control'})
        return form


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'class': 'form-control'})
        form.fields['password'].widget.attrs.update({'class': 'form-control'})
        return form


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        messages.success(request, _('Profile updated successfully'))
        return redirect('profile')
    return render(request, 'profile_edit.html')
