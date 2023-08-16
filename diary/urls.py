from django.contrib import admin
from django.urls import path, include

from exception_handler import forbidden_view, not_found_view, server_error_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.accounts.urls')),
    path('stories/', include('diary.stories.urls')),
    path('partners/', include('diary.partners.urls')),
]

handler400 = server_error_view
handler403 = forbidden_view
handler404 = not_found_view
handler500 = server_error_view
