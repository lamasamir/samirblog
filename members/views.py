from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy, reverse
from .forms  import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilepageForm
from django.contrib.auth.views import PasswordChangeView
from theblog.models import Profile

class UserRegisterView(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
  form_class = EditProfileForm
  template_name = 'registration/profile_edit.html'
  success_url = reverse_lazy('home') 

  def get_object(self):
    return self.request.user 
  
class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangingForm
  template_name='registration/change_password.html'
  # success_url = reverse_lazy('home')
  success_url = reverse_lazy('password_success')

def Password_sucess(request):
  return render(request, 'registration/password_success.html',{})  

class ShowProfilepageView(generic.DetailView):
  model = Profile
  template_name = 'registration/user_profile.html'
  
  def get_context_data(self, *args, **kwargs):
  #  users = Profile.objects.all()
   context = super(ShowProfilepageView, self).get_context_data(*args,**kwargs)
   page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
   context["page_user"] = page_user
   return context
  
class EditProfilepageView(generic.UpdateView):
  model = Profile
  template_name = 'registration/edit_profilepage.html' 
  fields = ['bio', 'profile_pic','website_url','facebook_url','instagram_url','twitter_url','pinterest_url']
  success_url = reverse_lazy('home')

class CreateProfilepageView(generic.CreateView):
  model = Profile
  form_class = ProfilepageForm
  template_name = 'registration/create_profile.html' 
  # fields  = '__all__'


  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  def get_success_url(self):
     return reverse('show_profile_page', kwargs={'pk': self.object.pk})
  
  
  
