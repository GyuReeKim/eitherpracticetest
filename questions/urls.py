from django.urls import path
from . import views

app_name ="questions"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),

    path('<int:id>/choices/create/', views.choice_create, name="choice_create"),
    path('<int:id1>/choices/<int:id2>/delete/', views.choice_delete, name="choice_delete"),
]
