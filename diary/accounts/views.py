from django.contrib.auth import views as auth_views, authenticate, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from .forms import RegisterUserForm

UserModel = get_user_model()


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return render(request, 'index_no_profile.html')



class UserRegistrationView(views.CreateView):
    template_name = 'profile\create-profile.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'profile\login-profile.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = 'profile\details-profile.html'
    model = UserModel


class ProfileEditView(views.UpdateView):
    template_name = 'profile\edit-profile.html'
    model = UserModel
    fields = ['profile_picture', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('index')


class ProfileDeleteView(views.DeleteView):
    template_name = 'profile\delete-profile.html'
    model = UserModel
    success_url = reverse_lazy('index')
