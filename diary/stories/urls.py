from django.urls import path, include

from diary.stories.views import my_stories, AddStoryView, detail_story, EditStoryView, DeleteStoryView

urlpatterns = (
    path('add/', AddStoryView.as_view(), name='add_story'),
    path('', my_stories, name='my_stories'),
    path('<int:pk>', detail_story, name='detail_story'),
    path('edit/<int:pk>', EditStoryView.as_view(), name='edit_story'),
    path('delete/<int:pk>', DeleteStoryView.as_view(), name='delete_story'),
    )
