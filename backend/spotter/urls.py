from django.urls import path

from . import views
app_name = "spotter"
urlpatterns = [
    path("", views.index, name="index"),
    path("detect_picture", views.detect_picture, name="detect_picture"),
    path("detect_batch_pictures", views.detect_batch_pictures, name="detect_batch_pictures"),
    path("create_video_detection_task", views.create_video_detection_task, name="create_video_detection_task"),
]