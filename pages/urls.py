from django.urls import path
from .views import HomePageView
from .views import second
from .views import yakwan


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("second/", second.as_view(), name="second"),
    path("yakwan/", yakwan.as_view(), name="yakwan")
]