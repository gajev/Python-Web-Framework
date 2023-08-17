from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from diary.partners.forms import PartnerUserForm
from diary.partners.models import PartnerUser
from django.views import generic as views


def is_authenticated_and_staff(user):
    return user.is_authenticated and user.is_staff


@login_required
def partners_view(request):
    life_partners = PartnerUser.objects.filter(type_partner=1)
    doctor_partners = PartnerUser.objects.filter(type_partner=2)
    love_partners = PartnerUser.objects.filter(type_partner=3)
    job_partners = PartnerUser.objects.filter(type_partner=4)
    context = {
        "life_partners": life_partners,
        "doctor_partners": doctor_partners,
        "love_partners": love_partners,
        "job_partners": job_partners,
    }
    return render(request, 'partners/partners.html', context)


class EditPartnersView(UserPassesTestMixin, views.UpdateView):
    template_name = 'partners/edit-partner.html'
    model = PartnerUser
    form_class = PartnerUserForm
    success_url = reverse_lazy('partners_view')

    def test_func(self):
        return is_authenticated_and_staff(self.request.user)


class DeletePartnersView(UserPassesTestMixin, views.DeleteView):
    template_name = 'partners/delete-partner.html'
    model = PartnerUser
    success_url = reverse_lazy('partners_view')

    def test_func(self):
        return is_authenticated_and_staff(self.request.user)
