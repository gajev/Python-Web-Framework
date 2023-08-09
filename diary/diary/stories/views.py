from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from diary.stories.forms import AddStoryForm, EditStoryForm
from diary.stories.models import Story
from datetime import datetime, timedelta

UserModel = get_user_model()


def check_enough_data(collection):
    n = 7
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
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class EditStoryView(views.UpdateView):
    template_name = 'stories/edit-story.html'
    model = Story
    form_class = EditStoryForm
    success_url = reverse_lazy('my_stories')


class DeleteStoryView(views.DeleteView):
    template_name = 'stories/delete-story.html'
    model = Story
    success_url = reverse_lazy('my_stories')


def my_stories(request):
    stories = Story.objects.filter(user=request.user)
    status = check_status(stories)
    context = {
        "stories": stories,
    }
    if status:
        context.update(status)
    return render(request, 'my_stories.html', context)


def detail_story(request, pk):
    stories = Story.objects.filter(pk=pk)
    context = {
        "story": stories[0],
    }
    return render(request, 'stories/details-story.html', context)
