from django.urls import path, include

from diary.accounts import views
from diary.accounts.views import index, UserRegistrationView, LoginUserView, LogoutUserView, \
    ProfileEditView, ProfileDeleteView, ProfileDetailsView


urlpatterns = (
    path('', index, name='index'),
    path('register/', UserRegistrationView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile_details'),
        path('edit/', ProfileEditView.as_view(), name='profile_edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    ]))

)