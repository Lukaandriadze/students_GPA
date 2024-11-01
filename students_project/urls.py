from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),  # Includes all URLs from students/urls.py
    path('__debug__/', include(debug_toolbar.urls)),
]
