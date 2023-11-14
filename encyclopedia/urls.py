from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_page_details, name="wiki"),
    path("search", views.search, name="search"),
    path("new", views.create, name='new-page')
]