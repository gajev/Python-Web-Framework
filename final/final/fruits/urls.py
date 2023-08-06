from django.urls import path, include

from final.fruits.views import index, dashboard, create_fruit, edit_fruit, delete_fruit, details_fruit, \
    edit_profile, details_profile, delete_profile, create_profile

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_fruit, name='create fruit'),
    path('<int:pk>/details/', details_fruit, name='details fruit'),
    path('<int:pk>/edit/', edit_fruit, name='edit fruit'),
    path('<int:pk>/delete/', delete_fruit, name='delete fruit'),

    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('edit/', edit_profile, name='edit profile')])),


)

