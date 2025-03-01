from django.urls import path

from . import views
app_name = "appadmin"
urlpatterns = [
    path("", views.index, name="index")

]