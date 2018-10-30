from django.conf import settings
from django.contrib import messages #
from django.contrib.auth import login as auth_login 
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, resolve_url
from .forms import SignupForm, ProfileForm

from django.views.generic import ListView, DetailView, TemplateView
from accounts.models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) 
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/profile_change_form.html'

    def get_object(self):
        return self.request.user.profile

class ProfileDeleteView(LoginRequiredMixin, DeleteView) :
    model = Profile
    success_url = reverse_lazy('home')

    #def get_object(self):
        #return self.request.user.delete()

class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/password_reset_form.html'
    
    def form_valid(self, form):
        messages.info(self.request, '암호 변경 메일을 발송했습니다.')
        return super().form_valid(form)

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/password_reset_confirm.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 리셋을 완료했습니다.')
        return super().form_valid(form)