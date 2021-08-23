from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SingUpForm, EditProfileForm, PasswordsChangingForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangingForm
    # from_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('home')

def password_success(request):
    return render(request, 'registration/password_success.html', {})   


class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

