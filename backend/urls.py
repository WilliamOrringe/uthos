from django.http import HttpResponse
from django.urls import path

from backend import views


urlpatterns = [
    path("", lambda _: HttpResponse("", status=200)),
    # Auth.
    path("start", views.start)


]
