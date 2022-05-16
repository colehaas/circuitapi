from django.urls import path, include, re_path
from . import views
from rest_framework import routers

app_name = 'trials'

router = routers.DefaultRouter()
router.register(r'trials', views.Studies, 'trial')

urlpatterns = [
    #path('', views.Studies.as_view(), name = 'studies'),
    path('', include(router.urls)),
    path('fullstudy/', views.CTAPI_FullStudy, name = 'fullstudy'),
]