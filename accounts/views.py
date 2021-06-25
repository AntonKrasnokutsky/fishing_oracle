from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic, View
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from .forms import UserNickEditForm
from fishing.getinfo import siteinfo, getuserinfo
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class RegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/registration.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['siteinfo'] = siteinfo()
        return context


class UserNickEdit(View):
    template = 'accounts/edit.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        user = request.user
        usernickeditform = UserNickEditForm(instance=user)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'usernickeditform':usernickeditform})
    
    def post (self, request, *args, **kwargs):
        user = request.user
        usernickeditform = UserNickEditForm(request.POST, instance=user)
        if usernickeditform.is_valid():
            user = usernickeditform.save(commit=False)
            user.save()
            return redirect('fishing:index')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                          'siteinfo': siteinfo(),
                          'usernickeditform':usernickeditform})
