from django.contrib import admin
from django.urls import path

from api.views import PersonView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', PersonView.as_view()),
]
