from django.urls import path

from diary.partners.views import partners_view, EditPartnersView, DeletePartnersView

urlpatterns = (
    path('', partners_view, name='partners_view'),
    path('edit/<int:pk>', EditPartnersView.as_view(), name='edit_partner'),
    path('delete/<int:pk>', DeletePartnersView.as_view(), name='delete_partner'),
)
