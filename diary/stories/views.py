from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from diary.stories.forms import AddStoryForm, EditStoryForm, TodoItemForm
from diary.stories.models import Story, TodoItem
from datetime import timedelta


UserModel = get_user_model()


def check_user_is_owner(current_object, current_request):
    if current_object.user_id != current_request.user.id:
        raise PermissionDenied


def check_enough_data(collection, n=7):
    if len(collection) < n or collection[0].date - timedelta(days=n-1) != collection[6].date:
        return False
    return True


def check_status(collection):
    if check_enough_data(collection):
        n = 7
        overall_sum = 0
        health_sum = 0
        love_sum = 0
        work_sum = 0
        for current_object in range(0, n):
            overall_sum += float(collection[current_object].overall)
            health_sum += float(collection[current_object].health)
            love_sum += float(collection[current_object].love)
            work_sum += float(collection[current_object].work)

        return {
            "overall_status": overall_sum / 7,
            "health_status": health_sum / 7,
            "love_status": love_sum / 7,
            "work_status": work_sum / 7,
        }


class AddStoryView(views.CreateView):
    template_name = 'stories/create-story.html'
    form_class = AddStoryForm
    success_url = reverse_lazy('my_stories')

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            return super().form_valid(form)
        except IntegrityError:
            default_image_path = "staticfiles/images/day_taken.png"
            with open(default_image_path, "rb") as default_image_file:
                default_image_data = default_image_file.read()

            current_response = HttpResponse(default_image_data, content_type='image/png', status=500)
            return current_response


class EditStoryView(views.UpdateView):

    template_name = 'stories/edit-story.html'
    model = Story
    form_class = EditStoryForm
    success_url = reverse_lazy('my_stories')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        check_user_is_owner(self.object, self.request)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.object = form.save()
            return super().form_valid(form)
        except IntegrityError:
            default_image_path = "staticfiles/images/day_taken.png"
            with open(default_image_path, "rb") as default_image_file:
                default_image_data = default_image_file.read()

            current_response = HttpResponse(default_image_data, content_type='image/png', status=500)
            return current_response


class DeleteStoryView(views.DeleteView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        check_user_is_owner(self.object, self.request)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    template_name = 'stories/delete-story.html'
    model = Story
    success_url = reverse_lazy('my_stories')


@login_required
def my_stories(request):
    stories = Story.objects.filter(user=request.user)
    status = check_status(stories)
    context = {
        "stories": stories,
    }
    if status:
        context.update(status)
    return render(request, 'stories/my_stories.html', context)


@login_required
def favorite_stories(request):
    stories = Story.objects.filter(user=request.user, favorite_story=True)
    context = {
        "stories": stories,
    }
    return render(request, 'stories/favorite_stories.html', context)


@login_required
def detail_story(request, pk):
    stories = Story.objects.filter(pk=pk)
    check_user_is_owner(stories[0], request)
    context = {
        "story": stories[0],
    }
    return render(request, 'stories/details-story.html', context)


class TodoListView(views.ListView):
    model = TodoItem
    template_name = 'stories/to_do_list.html'


class TodoCreateView(views.FormView):
    form_class = TodoItemForm
    template_name = 'stories/create-to-do.html'
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


