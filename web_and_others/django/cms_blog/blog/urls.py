from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("editor/", views.editor, name="editor"),
    path("editor/example-page/", views.example, name="example-page"),
    path("viewer/<int:username_id>/", views.viewer, name="viewer")
]