from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('frontend.urls')),
    #path('trials/', include('trials.urls')),
    re_path(r'^', include('trials.urls')),
]