from django.urls import include, path
from . import views
# users/urls.py
urlpatterns = [
    path('', views.Users.as_view()),
    path("myinfo/", views.MyInfo.as_view())
]