from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("add/",views.add,name = "add"),
    path("dashboard/",views.showArticle, name = "dashboard"),
    path("detail/<slug:slug>",views.detailArticle, name = "detail"),
    path("update/<slug:slug>",views.updateArticle, name = "update"),
    path("delete/<slug:slug>",views.deleteArticle, name = "delete"),
    path("find/",views.find,name="find"),
    path("comment/<int:id>",views.addComment,name = "comment"),
]