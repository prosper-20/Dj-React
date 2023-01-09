from django.urls import path
from .views import home,detail

urlpatterns = [
    path("home", home, name="home"),
    path("<int:pk>/", detail, name="detail")
]