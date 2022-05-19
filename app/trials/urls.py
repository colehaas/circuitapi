from django.urls import path, include, re_path
from . import views
from rest_framework import routers

app_name = 'trials'

router = routers.DefaultRouter()
router.register(r'trials', views.Studies, 'trial')

urlpatterns = [
    #path('', views.Studies.as_view(), name = 'studies'),
    path('', include(router.urls)),
    path('addstudy/', views.addStudy, name = 'addstudy'),
    path('preview/<expr>', views.preview, name = 'preview'),
]