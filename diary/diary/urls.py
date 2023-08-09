from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.accounts.urls')),
    path('stories/', include('diary.stories.urls')),
    path('partners/', include('diary.partners.urls')),
]

