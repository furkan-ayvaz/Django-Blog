from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("add/",views.add,name = "add"),
    path("dashboard/",views.showArticle, name = "dashboard"),
    path("detail/<int:id>",views.detailArticle, name = "detail"),
    path("update/<int:id>",views.updateArticle, name = "update"),
    path("delete/<int:id>",views.deleteArticle, name = "delete"),
    path("find/",views.find,name="find"),
    path("comment/<int:id>",views.addComment,name = "comment"),
]