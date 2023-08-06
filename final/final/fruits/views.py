from django.shortcuts import render, redirect
from django.views import generic as views


from final.fruits.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm
from final.fruits.models import Profile, Fruit


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def sum_posts():
    posts = 0
    for _ in Fruit.objects.all():
        posts += 1
    return posts


def index(request):
    profile = get_profile()
    if profile is None:
        return render(request, 'index_no_profile.html')
    return render(request, 'index.html')


def dashboard(request):
    context = {
        "fruits": Fruit.objects.all(),
    }
    return render(request, 'dashboard.html', context, )


def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
    }

    return render(request, 'fruit/create-fruit.html', context,)


def details_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    context = {
        'fruit': fruit,
    }
    return render(request, 'fruit/details-fruit.html', context,)


def edit_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruit/edit-fruit.html', context,)


def delete_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruit/delete-fruit.html', context, )



class RegisterUserView(views.CreateView):
    template_name = 'profile/create-profile.html'
    form_class = RegisterUserForm

    # Static way of providing `success_url`
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

def details_profile(request):
    posts = sum_posts()
    profile = get_profile()

    context = {
        'profile': profile,
        'posts': posts
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context, )


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        return render(request, 'profile/delete-profile.html')
    else:
        Fruit.objects.all().delete()
        profile.delete()
        return render(request, 'index_no_profile.html')




